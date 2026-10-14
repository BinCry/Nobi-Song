from collections.abc import Sequence
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from .domain import validate_artifact
from .models import AIImport, Photo, PhotoEmbedding, User
from .services import event_manager_access, record_audit


def import_artifact(db: Session, actor: User, artifact: dict) -> AIImport:
    errors = validate_artifact(artifact)
    if errors:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail=errors)
    try:
        event_id = UUID(artifact["event_id"])
    except ValueError as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "event_id must be a UUID") from exc
    event_manager_access(db, actor, event_id)
    photo_ids: list[UUID] = []
    vectors: list[Sequence[float]] = []
    for item in artifact["embeddings"]:
        try:
            photo_ids.append(UUID(item["photo_id"]))
        except ValueError as exc:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "photo_id must be a UUID") from exc
        vectors.append(item["vector"])
    if len(photo_ids) != len(set(photo_ids)):
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "photo_id appears more than once")
    if photo_ids:
        owned_photos = set(db.scalars(select(Photo.id).where(Photo.event_id == event_id, Photo.id.in_(photo_ids))))
        if owned_photos != set(photo_ids):
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "artifact contains photos outside this event")
    try:
        db.execute(update(AIImport).where(AIImport.event_id == event_id, AIImport.active.is_(True)).values(active=False))
        model = artifact["model"]
        imported = AIImport(event_id=event_id, model_name=model["name"], model_version=model["version"], schema_version=artifact["schema_version"], active=True)
        db.add(imported)
        db.flush()
        db.add_all(PhotoEmbedding(import_id=imported.id, photo_id=photo_id, embedding=list(vector)) for photo_id, vector in zip(photo_ids, vectors, strict=True))
        record_audit(db, actor.id, "ai.artifact_import", "event", event_id, "success")
        db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(imported)
    return imported
