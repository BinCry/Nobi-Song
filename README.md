
<div align="center">

# EventFace

**Private event-photo retrieval with consent-first face search.**

AI-powered face recognition for secure and intelligent event photo discovery.

<br>

<!-- Core Technologies -->
<p align="center">
  <img src="https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI_0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI 0.115">
  <img src="https://img.shields.io/badge/PostgreSQL_16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL 16">
</p>

<!-- AI and Infrastructure -->
<p align="center">
  <img src="https://img.shields.io/badge/pgvector-Enabled-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="pgvector">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/ONNX_Runtime-CPU-005F9E?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime CPU">
</p>

<!-- Architecture and Security -->
<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Modular-6E5494?style=flat-square" alt="Modular Architecture">
  <img src="https://img.shields.io/badge/Authentication-Google_OAuth-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google OAuth">
  <img src="https://img.shields.io/badge/AI_Inference-CPU_Only-FF6F00?style=flat-square" alt="CPU Inference">
</p>

</div>

---

## Overview

**EventFace** is an AI-powered event photo retrieval platform designed to help authorized attendees securely discover their own photos through facial recognition.

Users can authenticate with Google, select an authorized event, upload a selfie, and search for matching photos within that event's image collection.

The platform separates computationally intensive offline AI processing from lightweight online inference, enabling deployment on CPU-only infrastructure without requiring a dedicated GPU server.

### Core Capabilities

- **Offline AI Processing:** Google Colab supports dataset preparation, model training or fine-tuning when applicable, and face embedding extraction.
- **Online Face Recognition:** A compatible and properly licensed ONNX model performs facial inference on VPS CPU infrastructure.
- **Vector Similarity Search:** PostgreSQL with pgvector enables efficient, event-isolated face matching.
- **Privacy & Security:** Consent-first biometric processing, role-based authorization, and protected image storage are central architectural requirements.
- **Modular Architecture:** Clearly separated application components support maintainability and future extensions.

---

## Features

### Authentication & Authorization

- Google-only authentication integration.
- Secure cookie-based session configuration.
- Role-based access control (RBAC).
- Event-scoped authorization policies.
- Protected API endpoints.
- Role-specific permissions.

**Supported roles:**

| Role | Description |
|------|-------------|
| `USER` | Authorized attendee who can search for their own event photos. |
| `EVENT_MANAGER` | Manages assigned events and related photo resources. |
| `ADMIN` | Handles platform-level administration and authorization. |

### Event Management

- Event lifecycle and state management.
- Event-scoped management permissions.
- Event photo metadata management.
- Photo upload workflow.
- Private object storage integration.
- Signed storage access boundaries.
- Immutable audit event records.

### AI & Face Recognition

- Offline dataset preparation using Google Colab.
- Face detection and alignment.
- Face embedding extraction.
- ONNX Runtime CPU inference integration.
- Versioned AI artifact validation.
- Manual AI benchmark intake.
- Event-isolated cosine similarity search.
- PostgreSQL and pgvector integration.

### User Interface

- Responsive operator dashboard.
- Clean and consistent interface.
- Short and readable navigation labels.
- API health status monitoring.
- Clear loading, empty, and error states.
- No fabricated photo matches or performance claims.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI 0.115 |
| Database | PostgreSQL 16 |
| Vector Database Extension | pgvector |
| AI Inference Runtime | ONNX Runtime (CPU) |
| Offline AI Processing | Google Colab |
| Containerization | Docker Compose |
| Authentication | Google Identity |
| File Storage | S3-compatible Object Storage |
| Architecture | Modular Backend |

---

## Getting Started

### Prerequisites

Ensure the following tools are installed:

- Docker Engine
- Docker Compose
- Python 3.12 (for local development)
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd EventFace
```

Replace `<repository-url>` with the actual Git repository URL.

### 2. Configure Environment Variables

Create a local environment file from the provided template.

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS:**

```bash
cp .env.example .env
```

Configure the required environment variables according to `.env.example`.

Important configuration areas include:

- `GOOGLE_CLIENT_ID`
- `SESSION_SECRET`
- S3-compatible storage credentials
- Database connection settings
- Approved ONNX model configuration
- AI artifact paths and versions

> **Security Notice**
>
> Never commit real credentials, authentication secrets, private keys, or production environment files to version control.

### 3. Start with Docker

Build and start the application:

```bash
docker compose up --build
```

For detached execution:

```bash
docker compose up -d --build
```

Once the containers are running, open:

**Application URL:**

http://localhost:8000

The dashboard queries the following API endpoint for health information:

```http
GET /api/v1/health
```

> **Note**
>
> The application dashboard can be started independently of production AI readiness.
>
> Authentication, private storage access, and face-search functionality require valid credentials, appropriate storage configuration, and compatible approved AI model artifacts.
>
> The local URL assumes the Docker Compose configuration exposes the application on port `8000`.

---

## Local Development

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
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

Run the FastAPI development server:

```bash
uvicorn app.main:app --app-dir apps/api --reload
```

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation, when enabled:

http://127.0.0.1:8000/docs

### 5. Run Tests

Navigate to the backend directory:

```bash
cd apps/api
```

Execute the test suite:

```bash
pytest tests -q
```

> Some integration tests may require additional environment configuration, database services, storage dependencies, or test fixtures.

---

## System Architecture

EventFace uses a modular architecture that separates application responsibilities, persistent storage, and AI inference.

The architecture also separates offline GPU-assisted processing from online CPU inference.

### High-Level Architecture

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
    │ PostgreSQL 16  │ │  Private S3  │ │  ONNX Runtime  │
    │   + pgvector   │ │   Storage    │ │  CPU Inference │
    └────────────────┘ └──────────────┘ └────────────────┘
             ▲
             │
    ┌────────┴────────┐
    │  Validated AI   │
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

### Architecture Components

**Browser UI**

Provides the user-facing interface for authentication, event navigation, selfie submission, and photo retrieval.

**FastAPI Backend**

Handles application logic, request validation, authorization, event management, and AI inference orchestration.

**PostgreSQL + pgvector**

Stores structured application data and face embeddings used for similarity search.

**Private S3-compatible Storage**

Stores event photos and related media resources behind controlled access mechanisms.

**ONNX Runtime**

Executes compatible face recognition models using CPU inference.

**Google Colab**

Supports offline processing tasks such as dataset preparation, model evaluation, and large-scale face embedding extraction.

---

## AI Processing Workflow

EventFace uses separate offline and online AI pipelines.

This design reduces the computational requirements of the production VPS while maintaining a compatible face embedding workflow.

### Offline Pipeline — Google Colab

The offline pipeline prepares event photo embeddings before they are made available for online similarity search.

```text
          Event Photos
               │
               ▼
         Face Detection
               │
               ▼
         Face Alignment
               │
               ▼
    Face Embedding Extraction
               │
               ▼
       Artifact Validation
               │
               ▼
         Artifact Export
               │
               ▼
      Manual Artifact Import
               │
               ▼
      PostgreSQL + pgvector
```

**Offline responsibilities:**

1. Prepare and validate authorized event images.
2. Detect faces in event photos.
3. Align detected face regions.
4. Extract facial feature embeddings.
5. Validate embedding dimensions and model compatibility.
6. Export embeddings with associated image metadata.
7. Import validated embeddings into the appropriate event collection.

### Online Pipeline — VPS CPU

The online pipeline processes user selfies and searches for similar faces within an authorized event.

```text
            User Selfie
                │
                ▼
        Consent Verification
                │
                ▼
       Event Authorization
                │
                ▼
          Face Detection
                │
                ▼
          Face Alignment
                │
                ▼
       ONNX CPU Inference
                │
                ▼
          Face Embedding
                │
                ▼
      Vector Similarity Search
                │
                ▼
       Event-Scoped Filtering
                │
                ▼
        Similarity Evaluation
                │
                ▼
        Photo Match Results
                │
                ▼
     Authorized Photo Retrieval
```

**Online responsibilities:**

1. Verify user authentication and consent.
2. Confirm authorization for the selected event.
3. Validate the uploaded selfie.
4. Detect and align the face.
5. Generate a face embedding using ONNX Runtime.
6. Search for similar embeddings within the authorized event.
7. Apply configured similarity thresholds and matching policies.
8. Retrieve matching photo metadata.
9. Return authorized photo results to the user.

> **Model Compatibility**
>
> Offline and online embeddings must be generated using compatible preprocessing and embedding models.
>
> Model versions, embedding dimensions, alignment procedures, and normalization rules must remain consistent across both pipelines.
>
> Similarity thresholds must be selected using real evaluation data rather than arbitrary assumptions.

---

## Security & Privacy

EventFace is designed around privacy-conscious biometric data processing.

Facial images and biometric embeddings must be treated as sensitive personal information.

### Core Security Principles

- **Explicit Consent:** Obtain appropriate consent before processing biometric data.
- **Event Isolation:** Restrict searches and photo retrieval to authorized events.
- **Authentication:** Require verified user authentication.
- **Authorization:** Enforce role-based and resource-level access control.
- **Private Storage:** Prevent unrestricted public access to event images.
- **Protected Embeddings:** Secure biometric representations against unauthorized access.
- **Signed Access:** Use appropriately scoped, time-limited storage access where applicable.
- **Audit Logging:** Record security-relevant operations and administrative activity.
- **Retention Policies:** Define appropriate retention periods for images and biometric data.
- **Deletion Controls:** Support deletion workflows consistent with applicable requirements.

### Privacy Considerations

Biometric information is sensitive personal data.

Production deployments require appropriate:

1. Consent management.
2. Access control enforcement.
3. Data retention policies.
4. Secure storage and transmission.
5. Deletion and withdrawal procedures.
6. Privacy notices.
7. Applicable legal and regulatory review.

> **Important**
>
> Facial similarity does not guarantee identity.
>
> Search results should be treated as potential matches rather than definitive identity verification.
>
> A production deployment must evaluate the risks of false matches, unauthorized access, biometric data exposure, and misuse before enabling real-user processing.

---

## AI Models & Benchmarks

EventFace separates the application source code from external AI models, datasets, and benchmark artifacts.

### Repository Restrictions

This repository does not bundle:

- Proprietary or restricted model weights.
- Real biometric test fixtures.
- Unauthorized facial image datasets.
- Fabricated benchmark results.
- Production credentials or private secrets.

### Model Requirements

AI artifacts must satisfy the following requirements:

- Appropriate licensing for the intended use.
- Compatibility with ONNX Runtime where required.
- Consistent preprocessing and embedding specifications.
- Validated model input and output dimensions.
- Explicit artifact version information.
- Appropriate integrity and compatibility checks.

### Benchmark Requirements

Benchmark results must come from actual evaluations.

Relevant metrics may include:

| Metric | Purpose |
|--------|---------|
| Precision | Measures the proportion of returned matches that are correct. |
| Recall | Measures the proportion of relevant matches successfully retrieved. |
| False Acceptance Rate (FAR) | Measures the rate of incorrect positive identity decisions under a defined evaluation protocol. |
| False Rejection Rate (FRR) | Measures the rate of incorrect negative identity decisions under a defined evaluation protocol. |
| Inference Latency | Measures the time required for model inference. |
| Search Latency | Measures the time required for vector similarity retrieval. |
| Memory Usage | Measures runtime memory consumption. |

> No benchmark values should be presented without supporting test evidence, evaluation procedures, and clearly identified hardware conditions.

---

## Deployment Considerations

EventFace is designed to support deployment on CPU-only VPS infrastructure.

### Recommended Deployment Principles

- Run application services using Docker Compose.
- Keep PostgreSQL inaccessible from the public internet unless explicitly required and secured.
- Use private S3-compatible object storage.
- Configure HTTPS for production traffic.
- Protect session cookies with appropriate security settings.
- Store credentials outside the source code.
- Configure health checks and application logging.
- Validate ONNX model artifacts before loading them.
- Establish backup and recovery procedures.
- Restrict access to administrative operations.

### Offline vs. Online Processing

| Component | Execution Environment | Responsibility |
|-----------|-----------------------|----------------|
| Dataset Preparation | Google Colab | Prepare authorized image datasets |
| Face Embedding Extraction | Google Colab | Process event photo collections |
| Model Training / Fine-Tuning | Google Colab | Optional model adaptation and evaluation |
| API Backend | VPS | Application and business logic |
| Online Face Recognition | VPS CPU | Process user selfies |
| Vector Similarity Search | PostgreSQL + pgvector | Retrieve candidate matches |
| Photo Storage | S3-compatible Storage | Store and protect event images |

The exact hardware requirements depend on the selected models, event collection sizes, concurrent workloads, and actual benchmark results.

---

## Documentation

Additional technical documentation may be maintained separately for the following areas:

- **System Architecture** — Detailed components, responsibilities, and data flows.
- **AI Artifact Format** — Embedding specifications, metadata, validation rules, and model compatibility.
- **Deployment Guide** — Environment setup, production configuration, and operational requirements.
- **Test Report** — Functional testing, integration testing, performance evaluation, and benchmark evidence.

Documentation links should be added when the corresponding files are available in the repository.

---

## Project Principles

EventFace follows several core engineering principles:

1. **Privacy First:** Protect user images and biometric data.
2. **Consent First:** Require appropriate consent before biometric processing.
3. **Event Isolation:** Prevent unauthorized cross-event searches.
4. **Modular Design:** Separate application logic, storage, and AI inference.
5. **CPU-Friendly Deployment:** Avoid mandatory production GPU infrastructure.
6. **Reproducible Evaluation:** Report only verified benchmark results.
7. **Security by Design:** Apply authorization, data protection, and audit controls throughout the system.

---

<div align="center">

## EventFace

**Find your moments. Protect your identity.**

Private event-photo retrieval powered by AI.

Built with **Python · FastAPI · PostgreSQL · pgvector · ONNX Runtime**

</div>
