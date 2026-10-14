# VPS deployment

1. Copy `.env.example` to `.env` and replace every placeholder, especially `POSTGRES_PASSWORD`, `SESSION_SECRET`, Google OAuth values, and object-storage keys.
2. Put approved ONNX weights in a mounted private volume; do not add weights or credentials to Git.
3. Start `docker compose up --build`; apply `infrastructure/migrations/001_initial.sql` once against PostgreSQL.
4. Put Caddy or Nginx in front for HTTPS, set secure cookie settings, restrict database/object-storage ports, and back up the persistent database volume.

Before production, conduct privacy/legal review, verify OAuth callback URLs, exercise authorization tests against PostgreSQL, and measure retrieval quality on an authorized ground-truth dataset.
