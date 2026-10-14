# AI artifact contract

Artifacts are JSON and must contain `schema_version: "1.0"`, an `event_id`, a `model` object with `name` and `embedding_dimensions`, and embeddings containing only `photo_id` and `vector`. The server must verify that the artifact event matches the target event, every vector length matches the declared model dimension, photo IDs belong to that event, and the model is approved before activation.

The repository deliberately contains no face model, face data, or performance benchmark. Supply only licensed weights and consented fixtures.
