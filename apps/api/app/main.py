from pathlib import Path
from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from .core import EventStatus, Role, settings
from .database import get_db
from .domain import can_transition, validate_artifact
from .models import Event, User
from .schemas import AIImportRead, ArtifactRequest, EventCreate, EventRead
from .ai_service import import_artifact
from .security import current_user, require_role, verify_google_token
from .services import record_audit, transition_event

app = FastAPI(title="EventFace API", version="0.1.0", docs_url="/api/docs")
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret, https_only=settings.app_env == "production", same_site="lax")
app.add_middleware(CORSMiddleware, allow_origins=[item.strip() for item in settings.cors_allowed_origins.split(",")], allow_credentials=True, allow_methods=["GET", "POST", "PATCH", "DELETE"], allow_headers=["Content-Type", "X-CSRF-Token"])
static_dir = Path(__file__).parent / "static"
app.mount("/assets", StaticFiles(directory=static_dir), name="assets")


class TransitionRequest(BaseModel):
    current: EventStatus
    target: EventStatus
    has_valid_artifact: bool = False


class GoogleLoginRequest(BaseModel):
    credential: str = Field(min_length=20, max_length=10_000)


class EventTransitionRequest(BaseModel):
    target: EventStatus
    has_valid_artifact: bool = False


@app.get("/api/v1/health")
def health():
    return {"status": "ok", "service": "eventface-api", "inference": "configured" if Path(settings.ai_model_storage_path).is_file() else "not-configured"}


@app.post("/api/v1/auth/google")
def google_login(payload: GoogleLoginRequest, request: Request, db: Session = Depends(get_db)):
    claims = verify_google_token(payload.credential)
    user = db.scalar(select(User).where(User.google_sub == claims["sub"]))
    if not user:
        user = User(google_sub=claims["sub"], email=claims["email"], role=Role.USER)
        db.add(user)
        db.flush()
        record_audit(db, user.id, "auth.google_login", "user", user.id, "created")
    if user.disabled_at:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Account is disabled")
    request.session.clear()
    request.session["user_id"] = str(user.id)
    record_audit(db, user.id, "auth.google_login", "user", user.id, "success")
    db.commit()
    return {"id": user.id, "role": user.role}


@app.post("/api/v1/auth/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(request: Request):
    request.session.clear()


@app.post("/api/v1/events", response_model=EventRead, status_code=status.HTTP_201_CREATED)
def create_event(payload: EventCreate, db: Session = Depends(get_db), actor: User = Depends(require_role(Role.EVENT_MANAGER, Role.ADMIN))):
    if db.scalar(select(Event).where(Event.slug == payload.slug)):
        raise HTTPException(status.HTTP_409_CONFLICT, "Event slug already exists")
    event = Event(**payload.model_dump(), owner_id=actor.id)
    db.add(event)
    db.flush()
    record_audit(db, actor.id, "event.create", "event", event.id, "success")
    db.commit()
    db.refresh(event)
    return event


@app.get("/api/v1/events", response_model=list[EventRead])
def list_events(db: Session = Depends(get_db), actor: User = Depends(current_user)):
    if actor.role is Role.ADMIN:
        return list(db.scalars(select(Event).order_by(Event.created_at.desc())))
    return list(db.scalars(select(Event).where(Event.owner_id == actor.id).order_by(Event.created_at.desc())))


@app.post("/api/v1/events/{event_id}/transition", response_model=EventRead)
def change_event_status(event_id: UUID, payload: EventTransitionRequest, db: Session = Depends(get_db), actor: User = Depends(require_role(Role.EVENT_MANAGER, Role.ADMIN))):
    return transition_event(db, actor, event_id, payload.target, payload.has_valid_artifact)


@app.post("/api/v1/ai/artifacts/validate")
def validate_ai_artifact(request: ArtifactRequest, actor: User = Depends(require_role(Role.EVENT_MANAGER, Role.ADMIN))):
    errors = validate_artifact(request.model_dump())
    return {"valid": not errors, "errors": errors}


@app.post("/api/v1/ai/artifacts/import", response_model=AIImportRead, status_code=status.HTTP_201_CREATED)
def import_ai_artifact(request: ArtifactRequest, db: Session = Depends(get_db), actor: User = Depends(require_role(Role.EVENT_MANAGER, Role.ADMIN))):
    return import_artifact(db, actor, request.model_dump())


@app.get("/")
def dashboard():
    return FileResponse(static_dir / "index.html")
