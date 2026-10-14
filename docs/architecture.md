# Architecture

The API is a modular monolith. Browser requests pass through a reverse proxy to FastAPI, which enforces authenticated role and event scope before accessing PostgreSQL, private object storage, or the inference module.

The online path is `selfie → approved ONNX Runtime CPU model → normalized embedding → event-scoped pgvector query → authorized signed photo URL`. Google Colab is never called from this path.

The offline path is `event photos → manifest export → Colab processing → artifact → manager import → schema/model validation → atomic index activation`. A failed import must not replace an active import.
