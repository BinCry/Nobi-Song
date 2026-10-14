# EventFace

<p align="center">
  <strong>Private event-photo retrieval with consent-first face search.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/pgvector-enabled-4B8BBE" alt="pgvector" />
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/ONNX_Runtime-CPU-005CED" alt="ONNX Runtime" />
</p>

EventFace helps approved attendees retrieve their own event photos. A trained, licensed ONNX model runs inference on the VPS CPU; offline dataset preparation and embedding extraction happen separately in Google Colab.

## What is included

- Google-only identity verification hook with secure cookie-session configuration.
- Role and event-scoped authorization primitives (`USER`, `EVENT_MANAGER`, `ADMIN`).
- Event lifecycle rules, safe photo metadata upload, signed-storage integration boundary, and immutable audit events.
- Versioned AI artifact validation, benchmark intake, and event-isolated cosine search contract.
- A responsive operator UI with short, one-line labels; no invented photo matches or performance claims.
- PostgreSQL + pgvector Docker environment and a migration for the core schema.

## Start locally

```bash
copy .env.example .env
docker compose up --build
```

Open `http://localhost:8000`. The interactive dashboard queries `/api/v1/health` directly. Configure `GOOGLE_CLIENT_ID`, a strong `SESSION_SECRET`, S3 credentials, and an approved ONNX model before enabling identity or face-search flows.

## Development

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r apps/api/requirements.txt
uvicorn app.main:app --app-dir apps/api --reload
cd apps/api
pytest tests -q
```

## Architecture

```
Browser UI -> FastAPI -> PostgreSQL + pgvector
                    -> private S3-compatible object storage
                    -> ONNX Runtime CPU inference

Event photos -> Google Colab (offline) -> validated artifact import -> pgvector index
```

All biometric material is sensitive: do not expose embeddings or public buckets, use consent and retention controls, and obtain legal/privacy review for the jurisdictions where events operate. No model weights, real biometric fixtures, or benchmark results are bundled in this repository.

See [architecture](docs/architecture.md), [AI artifact format](docs/ai-artifact.md), [deployment](docs/deployment.md), and the [test report](docs/test-report.md).
