CREATE EXTENSION IF NOT EXISTS vector;

CREATE TYPE user_role AS ENUM ('USER', 'EVENT_MANAGER', 'ADMIN');
CREATE TYPE event_status AS ENUM ('DRAFT', 'UPLOADING', 'PROCESSING', 'AWAITING_IMPORT', 'VALIDATING', 'READY', 'PUBLISHED', 'ARCHIVED', 'FAILED', 'NEEDS_ACTION');

CREATE TABLE users (
  id UUID PRIMARY KEY, google_sub TEXT UNIQUE NOT NULL, email TEXT NOT NULL,
  role user_role NOT NULL DEFAULT 'USER', disabled_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE events (
  id UUID PRIMARY KEY, slug TEXT UNIQUE NOT NULL, title TEXT NOT NULL, status event_status NOT NULL DEFAULT 'DRAFT',
  owner_id UUID NOT NULL REFERENCES users(id), description TEXT, retention_days INTEGER NOT NULL DEFAULT 90, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE event_managers (event_id UUID REFERENCES events(id), user_id UUID REFERENCES users(id), PRIMARY KEY(event_id, user_id));
CREATE TABLE photos (
  id UUID PRIMARY KEY, event_id UUID NOT NULL REFERENCES events(id), object_key TEXT UNIQUE NOT NULL, sha256 CHAR(64) NOT NULL,
  original_name TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), UNIQUE(event_id, sha256)
);
CREATE TABLE ai_imports (
  id UUID PRIMARY KEY, event_id UUID NOT NULL REFERENCES events(id), model_name TEXT NOT NULL, model_version TEXT NOT NULL,
  schema_version TEXT NOT NULL, active BOOLEAN NOT NULL DEFAULT FALSE, imported_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE photo_embeddings (
  import_id UUID NOT NULL REFERENCES ai_imports(id), photo_id UUID NOT NULL REFERENCES photos(id), embedding vector(512) NOT NULL,
  PRIMARY KEY(import_id, photo_id)
);
CREATE INDEX photo_embeddings_vector_idx ON photo_embeddings USING hnsw (embedding vector_cosine_ops);
CREATE TABLE audit_logs (id UUID PRIMARY KEY, actor_id UUID REFERENCES users(id), action TEXT NOT NULL, resource_type TEXT NOT NULL, resource_id UUID, outcome TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL DEFAULT now());
