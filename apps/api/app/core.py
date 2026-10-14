from enum import StrEnum
from pydantic_settings import BaseSettings, SettingsConfigDict


class Role(StrEnum):
    USER = "USER"
    EVENT_MANAGER = "EVENT_MANAGER"
    ADMIN = "ADMIN"


class EventStatus(StrEnum):
    DRAFT = "DRAFT"
    UPLOADING = "UPLOADING"
    PROCESSING = "PROCESSING"
    AWAITING_IMPORT = "AWAITING_IMPORT"
    VALIDATING = "VALIDATING"
    READY = "READY"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"
    FAILED = "FAILED"
    NEEDS_ACTION = "NEEDS_ACTION"


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite://"
    google_client_id: str = ""
    session_secret: str = "development-only-change-me"
    cors_allowed_origins: str = "http://localhost:8000"
    ai_model_storage_path: str = "/models/approved-face-model.onnx"
    max_upload_size: int = 20 * 1024 * 1024
    default_data_retention_days: int = 90
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
