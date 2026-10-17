# CaseHop

**CaseHop — Switch models with confidence.**

CaseHop compares the model behind a small SaaS's structured-output feature with two
open-weight alternatives using the team's reviewed application cases. It exposes
consequential failures, preserves uncertainty, produces a limited TRY/HOLD/REJECT
verdict, and generates a controlled Hop Plan grounded only in observed evidence.

See `docs/HANDOFF.md` for the full product and engineering contract.

## Local development

### Prerequisites

- Node.js 24 LTS
- Python 3.12

### Backend

```bash
python3.12 -m venv .venv
./.venv/bin/python -m pip install -r backend/requirements-dev.txt
./.venv/bin/python -m uvicorn app.main:app --reload --app-dir backend
```

Health check: `http://localhost:8000/api/v1/health`

### Frontend

```bash
npm --prefix frontend ci
npm --prefix frontend run dev
```

App: `http://localhost:5173`

### Quality commands

Backend:

```bash
./.venv/bin/python -m ruff check backend
./.venv/bin/python -m ruff format --check backend
./.venv/bin/python -m mypy backend/app
./.venv/bin/python -m pytest backend/tests -q
```

Frontend:

```bash
npm --prefix frontend run lint
npm --prefix frontend run typecheck
npm --prefix frontend run test -- --run
npm --prefix frontend run build
npm --prefix frontend run test:e2e
```

## Status

Stack foundation in progress. See `docs/EXECUTION_STATE.md`.
