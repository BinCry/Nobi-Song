from app.core import EventStatus, Role
from app.domain import can_transition, may_manage_event, validate_artifact


def test_publish_requires_valid_artifact():
    assert not can_transition(EventStatus.READY, EventStatus.PUBLISHED)
    assert can_transition(EventStatus.READY, EventStatus.PUBLISHED, True)


def test_event_manager_cannot_manage_unassigned_event():
    assert not may_manage_event(Role.EVENT_MANAGER, False)
    assert may_manage_event(Role.EVENT_MANAGER, True)
    assert may_manage_event(Role.ADMIN, False)


def test_artifact_requires_consistent_embedding_dimensions():
    artifact = {"schema_version": "1.0", "event_id": "event-1", "model": {"name": "approved.onnx", "version": "1", "embedding_dimensions": 512}, "embeddings": [{"photo_id": "photo-1", "vector": [0.1, 0.2]}]}
    assert "embedding dimension mismatch" in validate_artifact(artifact)
