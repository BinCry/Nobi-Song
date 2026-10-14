# Test report — 2026-10-14

| Check | Result | Evidence |
| --- | --- | --- |
| Unit and API tests | Passed | `pytest tests -q`: 5 passed. |
| Dependency integrity | Passed | `pip check`: no broken requirements. |
| Python syntax compilation | Passed | `python -m compileall -q apps/api/app` completed successfully. |
| HTTP smoke test | Passed | `GET /api/v1/health`: 200; `GET /`: 200 and returned EventFace dashboard. |
| Compose YAML | Passed | Parsed by PyYAML. |
| Docker Compose runtime | Not run | Docker CLI is not installed in this environment. |

The Docker/runtime check remains the only local verification gap. Start it in a Docker-equipped environment with `docker compose up --build`.
