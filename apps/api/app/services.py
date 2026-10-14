from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from .core import EventStatus, Role
from .domain import can_transition, may_manage_event
from .models import AuditLog, Event, EventManager, User


def event_manager_access(db: Session, actor: User, event_id: UUID) -> Event:
    event = db.get(Event, event_id)
    if not event:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Event not found")
    assigned = db.scalar(select(EventManager).where(EventManager.event_id == event_id, EventManager.user_id == actor.id)) is not None
    if not may_manage_event(actor.role, assigned):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Not allowed for this event")
    return event


def record_audit(db: Session, actor_id: UUID | None, action: str, resource_type: str, resource_id: UUID | None, outcome: str) -> None:
    db.add(AuditLog(actor_id=actor_id, action=action, resource_type=resource_type, resource_id=resource_id, outcome=outcome))


def transition_event(db: Session, actor: User, event_id: UUID, target: EventStatus, has_valid_artifact: bool) -> Event:
    event = event_manager_access(db, actor, event_id)
    if not can_transition(event.status, target, has_valid_artifact):
        record_audit(db, actor.id, "event.transition", "event", event.id, "denied")
        db.commit()
        raise HTTPException(status.HTTP_409_CONFLICT, "This event transition is not permitted")
    event.status = target
    record_audit(db, actor.id, "event.transition", "event", event.id, "success")
    db.commit()
    db.refresh(event)
    return event
