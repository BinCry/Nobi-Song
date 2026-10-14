from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, field_validator
from .core import EventStatus


class EventCreate(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    description: str | None = Field(default=None, max_length=2000)
    retention_days: int = Field(default=90, ge=1, le=3650)


class EventRead(BaseModel):
    id: UUID
    title: str
    slug: str
    status: EventStatus
    retention_days: int
    created_at: datetime
    model_config = {"from_attributes": True}


class ArtifactRequest(BaseModel):
    schema_version: str
    event_id: str
    model: dict
    embeddings: list[dict] = Field(default_factory=list)

    @field_validator("embeddings")
    @classmethod
    def limit_embeddings(cls, value: list[dict]):
        if len(value) > 20_000:
            raise ValueError("artifact exceeds maximum batch size")
        return value


class AIImportRead(BaseModel):
    id: UUID
    event_id: UUID
    model_name: str
    model_version: str
    schema_version: str
    active: bool
    created_at: datetime = Field(alias="imported_at")
    model_config = {"from_attributes": True, "populate_by_name": True}
