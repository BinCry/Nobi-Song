from .core import EventStatus, Role

TRANSITIONS = {
    EventStatus.DRAFT: {EventStatus.UPLOADING, EventStatus.ARCHIVED},
    EventStatus.UPLOADING: {EventStatus.PROCESSING, EventStatus.NEEDS_ACTION},
    EventStatus.PROCESSING: {EventStatus.AWAITING_IMPORT, EventStatus.FAILED},
    EventStatus.AWAITING_IMPORT: {EventStatus.VALIDATING, EventStatus.NEEDS_ACTION},
    EventStatus.VALIDATING: {EventStatus.READY, EventStatus.NEEDS_ACTION},
    EventStatus.READY: {EventStatus.PUBLISHED, EventStatus.ARCHIVED},
    EventStatus.PUBLISHED: {EventStatus.ARCHIVED},
    EventStatus.NEEDS_ACTION: {EventStatus.UPLOADING, EventStatus.AWAITING_IMPORT},
    EventStatus.FAILED: {EventStatus.UPLOADING, EventStatus.ARCHIVED},
    EventStatus.ARCHIVED: set(),
}


def can_transition(current: EventStatus, target: EventStatus, has_valid_artifact: bool = False) -> bool:
    if target not in TRANSITIONS[current]:
        return False
    return not (target is EventStatus.PUBLISHED and not has_valid_artifact)


def may_manage_event(role: Role, is_assigned_manager: bool) -> bool:
    return role is Role.ADMIN or (role is Role.EVENT_MANAGER and is_assigned_manager)


def validate_artifact(payload: dict) -> list[str]:
    required = {"schema_version", "event_id", "model", "embeddings"}
    errors = [f"missing {key}" for key in sorted(required - payload.keys())]
    if payload.get("schema_version") != "1.0":
        errors.append("unsupported schema_version")
    model = payload.get("model") or {}
    if not model.get("name") or not model.get("version") or not model.get("embedding_dimensions"):
        errors.append("model name, version and embedding_dimensions are required")
    if model.get("embedding_dimensions") != 512:
        errors.append("only 512-dimensional approved embeddings are supported")
    for item in payload.get("embeddings", []):
        if not item.get("photo_id") or not isinstance(item.get("vector"), list):
            errors.append("each embedding requires photo_id and vector")
            break
        if model.get("embedding_dimensions") and len(item["vector"]) != model["embedding_dimensions"]:
            errors.append("embedding dimension mismatch")
            break
    return errors
