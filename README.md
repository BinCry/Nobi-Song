
<div align="center">

# EventFace

**Private event-photo retrieval with consent-first face search.**

AI-powered face recognition for secure and intelligent event photo discovery.


Conversation with Gemini
<br/>



<img src="https://img.shields.io/badge/Python_3.12-161B22?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python 3.12" />

<img src="https://img.shields.io/badge/FastAPI_0.115-161B22?style=for-the-badge&logo=fastapi&logoColor=00C7B7" alt="FastAPI" />

<img src="https://img.shields.io/badge/PostgreSQL_16-161B22?style=for-the-badge&logo=postgresql&logoColor=60A5FA" alt="PostgreSQL 16" />



<br/>



<img src="https://img.shields.io/badge/pgvector-Enabled-161B22?style=for-the-badge&logo=postgresql&logoColor=60A5FA" alt="pgvector" />

<img src="https://img.shields.io/badge/Docker-Ready-161B22?style=for-the-badge&logo=docker&logoColor=2496ED" alt="Docker" />

<img src="https://img.shields.io/badge/ONNX_Runtime-CPU-161B22?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime CPU" />



<br/>



<img src="https://img.shields.io/badge/Architecture-Modular-21262D?style=flat-square" alt="Modular Architecture" />

<img src="https://img.shields.io/badge/Authentication-Google_OAuth-21262D?style=flat-square&logo=google&logoColor=white" alt="Google OAuth" />

<img src="https://img.shields.io/badge/AI_Inference-CPU_Only-21262D?style=flat-square" alt="CPU Inference" />



</div>



---



## Overview



**EventFace** is an AI-powered event photo retrieval platform that helps approved attendees discover their own photos through face recognition

Sửa cho hiển thị đều và đẹp trên mobile và laptop

Để các thẻ Badge (huy hiệu) hiển thị đều, đẹp và căn chỉnh hoàn hảo trên cả máy tính (laptop) và điện thoại (mobile), cách tốt nhất là nhóm chúng vào một thẻ <div> bọc ngoài và sử dụng Flexbox với thuộc tính flex-wrap: wrap và khoảng cách hợp lý (gap). Điều này giúp các badge tự động xuống dòng gọn gàng trên màn hình nhỏ mà không bị tràn viền hay lệch lạc.

Dưới đây là phần code HTML đã được tối ưu lại giao diện cho cả mobile và laptop:

HTML
<div align="center">

  <!-- Nhóm các badge công nghệ cốt lõi -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-bottom: 8px;">
    <img src="https://img.shields.io/badge/Python_3.12-161B22?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python 3.12" />
    <img src="https://img.shields.io/badge/FastAPI_0.115-161B22?style=for-the-badge&logo=fastapi&logoColor=00C7B7" alt="FastAPI" />
    <img src="https://img.shields.io/badge/PostgreSQL_16-161B22?style=for-the-badge&logo=postgresql&logoColor=60A5FA" alt="PostgreSQL 16" />
  </div>

  <!-- Nhóm các badge tính năng & hạ tầng -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-bottom: 12px;">
    <img src="https://img.shields.io/badge/pgvector-Enabled-161B22?style=for-the-badge&logo=postgresql&logoColor=60A5FA" alt="pgvector" />
    <img src="https://img.shields.io/badge/Docker-Ready-161B22?style=for-the-badge&logo=docker&logoColor=2496ED" alt="Docker" />
    <img src="https://img.shields.io/badge/ONNX_Runtime-CPU-161B22?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime CPU" />
  </div>

  <!-- Nhóm các badge thông tin kiến trúc (style flat-square nhỏ gọn hơn) -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; margin-bottom: 16px;">
    <img src="https://img.shields.io/badge/Architecture-Modular-21262D?style=flat-square" alt="Modular Architecture" />
    <img src="https://img.shields.io/badge/Authentication-Google_OAuth-21262D?style=flat-square&logo=google&logoColor=white" alt="Google OAuth" />
    <img src="https://img.shields.io/badge/AI_Inference-CPU_Only-21262D?style=flat-square" alt="CPU Inference" />
  </div>

</div>

---
---

## Overview

**EventFace** is an AI-powered event photo retrieval platform that helps approved attendees discover their own photos through face recognition.

Users can authenticate with Google, select an authorized event, upload a selfie, and search for matching photos within that event's image collection.

The system separates offline AI processing from online inference to support deployment on CPU-only infrastructure.

- **Offline AI Processing:** Google Colab handles dataset preparation, model training or fine-tuning when applicable, and face embedding extraction.
- **Online Face Recognition:** A compatible, licensed ONNX model performs inference on the VPS CPU.
- **Vector Similarity Search:** PostgreSQL with pgvector enables event-isolated face matching.
- **Privacy & Security:** Consent, role-based authorization, and protected image storage are core architectural requirements.

## Features

### Authentication & Authorization

- Google-only identity verification hook.
- Secure cookie-session configuration.
- Role-based access control (RBAC).
- Event-scoped authorization.
- Supported roles: `USER`, `EVENT_MANAGER`, `ADMIN`.

### Event Management

- Event lifecycle rules and state management.
- Event-scoped management permissions.
- Photo metadata upload workflow.
- Signed-storage integration boundary.
- Immutable audit events.

### AI & Face Recognition

- Offline dataset preparation with Google Colab.
- ONNX Runtime CPU inference integration.
- Versioned AI artifact validation.
- Manual benchmark intake.
- Event-isolated cosine similarity search.
- PostgreSQL and pgvector integration.

### User Interface

- Responsive operator dashboard.
- Clean and consistent interface.
- Short, readable labels.
- API health monitoring.
- No fabricated photo matches or performance claims.

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Backend | FastAPI 0.115 |
| Database | PostgreSQL 16 |
| Vector Search | pgvector |
| AI Runtime | ONNX Runtime (CPU) |
| Offline AI Processing | Google Colab |
| Containerization | Docker Compose |
| Authentication | Google Identity |
| Storage | S3-compatible Object Storage |

## Getting Started

### Prerequisites

Ensure the following tools are installed:

- Docker and Docker Compose
- Python 3.12 (for local development)
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd EventFace
```

Replace `<repository-url>` with the actual repository URL.

### 2. Configure Environment Variables

Create an environment file from the provided template.

**Windows:**

```powershell
copy .env.example .env
```

**Linux / macOS:**

```bash
cp .env.example .env
```

Configure the required environment variables:

- `GOOGLE_CLIENT_ID`
- `SESSION_SECRET`
- S3 storage credentials
- Approved ONNX model configuration

Do not commit real secrets to version control.

### 3. Start with Docker

```bash
docker compose up --build
```

Once the containers are running, open:

**http://localhost:8000**

The interactive dashboard queries `/api/v1/health` directly.

Identity and face-search flows require valid credentials, storage configuration, and compatible approved model artifacts before they can be enabled.

## Local Development

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Environment

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r apps/api/requirements.txt
```

### 4. Start the Backend

```bash
uvicorn app.main:app --app-dir apps/api --reload
```

### 5. Run Tests

```bash
cd apps/api
pytest tests -q
```

## System Architecture

```text
                    ┌─────────────────────┐
                    │     Browser UI      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    │  Auth · Events · AI │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
    ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
    │ PostgreSQL 16  │ │ Private S3   │ │ ONNX Runtime   │
    │   + pgvector   │ │   Storage    │ │  CPU Inference │
    └────────────────┘ └──────────────┘ └────────────────┘
             ▲
             │
    ┌────────┴────────┐
    │ Validated AI    │
    │ Artifact Import │
    └────────┬────────┘
             ▲
             │
    ┌─────────────────┐
    │  Google Colab   │
    │ Offline AI/GPU  │
    └────────┬────────┘
             ▲
             │
    ┌─────────────────┐
    │  Event Photos   │
    └─────────────────┘
```

### AI Processing Workflow

**Offline Pipeline – Google Colab**

```text
Event Photos
    ↓
Face Detection
    ↓
Face Alignment
    ↓
Face Embedding Extraction
    ↓
Artifact Export
    ↓
Manual Artifact Import
    ↓
PostgreSQL + pgvector
```

**Online Pipeline – VPS CPU**

```text
User Selfie
    ↓
Face Detection
    ↓
ONNX CPU Inference
    ↓
Face Embedding
    ↓
Vector Similarity Search
    ↓
Event Photo Matching
    ↓
Photo Retrieval Results
```

## Security & Privacy

EventFace is designed around privacy-conscious biometric data processing.

Key security considerations include:

- Explicit consent before face search.
- Event-scoped access control.
- Secure authentication and authorization.
- Private object storage.
- Protected biometric embeddings.
- Restricted image access.
- Audit logging.
- Data retention and deletion controls.

> **Important:** Biometric information is sensitive personal data. Deployments require appropriate consent, access controls, retention policies, and legal/privacy review for the jurisdictions in which events operate.

## AI Models & Benchmarks

This repository does not bundle:

- Proprietary or restricted model weights.
- Real biometric test fixtures.
- Fabricated benchmark results.
- Production credentials.

Model artifacts must be legally licensed, validated, and compatible with the CPU inference runtime.

Benchmark results must be derived from actual evaluations rather than assumed performance.

## Documentation

Additional technical documentation:

- [System Architecture](docs/architecture.md)
- [AI Artifact Format](docs/ai-artifact.md)
- [Deployment Guide](docs/deployment.md)
- [Test Report](docs/test-report.md)

---

<div align="center">

**EventFace**

*Find your moments. Protect your identity.*

Built with Python, FastAPI, PostgreSQL, pgvector, and ONNX Runtime.

</div>
