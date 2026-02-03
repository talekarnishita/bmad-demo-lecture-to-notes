# Architecture: Dev Demo

**Date:** 2026-01-28  
**Author:** Nishitatalekar

This document describes the technical architecture of the Dev demo (Option B: minimal web app). For the reasoning behind these choices, see [TECHNICAL_APPROACH.md](./TECHNICAL_APPROACH.md).

---

## High-Level Architecture

```
┌─────────────┐     upload      ┌──────────────────┐     transcribe     ┌─────────────┐
│   Browser   │ ──────────────► │  FastAPI (demo)  │ ─────────────────► │ Whisper API │
│ (index.html)│                 │  POST /process   │                     │ (OpenAI)    │
└─────────────┘                 └────────┬───────┘                     └──────┬──────┘
       ▲                                  │                                    │
       │                                  │ transcript                         │
       │                                  ▼                                    │
       │                          ┌───────────────┐     structure                │
       │                          │  Temp file    │ ◄──────────────────────────┘
       │                          │  (deleted)    │
       │                          └───────┬───────┘
       │                                  │
       │                                  │ prompt
       │                                  ▼
       │                          ┌─────────────┐
       │     JSON response        │  GPT-4o-mini│
       └──────────────────────────│  (OpenAI)   │
                                  └─────────────┘
```

**Flow:** User uploads file → backend saves to temp file → Whisper transcribes → GPT structures transcript → JSON returned → frontend renders. Temp file is deleted; nothing is persisted.

---

## Components

### 1. Frontend (static)

| Component | Location | Responsibility |
|-----------|----------|----------------|
| **UI** | `static/index.html` | Single page: file input, drag-and-drop, "Processing…" state, render sections/summary/key concepts |
| **Logic** | Inline JavaScript | Upload via `FormData`, call `POST /process`, display result or error |
| **No build** | — | Vanilla HTML/JS; no framework or bundler |

**Entry:** `GET /` serves `static/index.html`.

### 2. Backend (FastAPI)

| Component | Location | Responsibility |
|-----------|----------|----------------|
| **App** | `app.py` | FastAPI app, routes, env config |
| **Routes** | `app.py` | `GET /` → serve UI; `POST /process` → accept file, call APIs, return JSON |
| **Config** | `.env` (not in repo) | `OPENAI_API_KEY`, optional `MAX_UPLOAD_BYTES` (default 25MB) |

**Entry:** `uvicorn app:app --reload` → listens on `http://127.0.0.1:8000` by default.

### 3. External Services

| Service | Purpose | Constraint |
|---------|---------|------------|
| **OpenAI Whisper API** | Transcribe audio/video to text | 25MB max file size |
| **OpenAI GPT-4o-mini** | Turn transcript into structured JSON (sections, summary, keyConcepts) | Same API key as Whisper |

**Credentials:** Read from environment (`OPENAI_API_KEY`); never hardcoded.

---

## Data Flow

### Request Path

1. **User** selects or drops a file (mp3, mp4, m4a, wav, webm, etc.).
2. **Frontend** sends `multipart/form-data` to `POST /process`.
3. **Backend**:
   - Validates file size (≤ `MAX_UPLOAD_BYTES`) and extension.
   - Writes body to a temp file.
   - Calls Whisper API → receives transcript text.
   - Builds prompt from `STRUCTURE_PROMPT` + transcript.
   - Calls GPT-4o-mini → receives JSON.
   - Validates JSON has `summary`, `sections`, `keyConcepts`.
   - Deletes temp file.
   - Returns JSON response.
4. **Frontend** renders sections, summary, and key concepts (and optional download/copy).

### Response Shape

```json
{
  "summary": "Short paragraph of main ideas.",
  "sections": [
    { "heading": "Section title", "content": "Bullets or short paragraph." }
  ],
  "keyConcepts": ["term1", "term2", { "term": "x", "definition": "y" }]
}
```

Defined in `app.py` via `STRUCTURE_PROMPT` and validated before response.

---

## Repository Structure

```
demo/
├── app.py                 # FastAPI app, GET /, POST /process
├── requirements.txt       # fastapi, uvicorn, openai, python-dotenv, etc.
├── .env.example          # Template for OPENAI_API_KEY, MAX_UPLOAD_BYTES
├── .gitignore            # .env, .venv, __pycache__, etc.
├── static/
│   └── index.html        # Single-page UI
├── architecture.md       # This file
├── TECHNICAL_APPROACH.md # Why this architecture was chosen
├── CODE_MAPPING.md       # How code implements BMAD decisions
├── PRD.md                # Scope, success criteria (concise)
├── PRODUCT_BRIEF.md      # Problem, user, goal (concise)
└── bmad-output/         # Full BMAD planning artifacts
    ├── README.md
    └── planning-artifacts/
        ├── product-brief-Dev-2026-01-28.md
        ├── prd.md
        └── demo-technical-approach.md
```

---

## Technology Stack

| Layer | Technology | Version / notes |
|-------|------------|-----------------|
| **Runtime** | Python 3.x | 3.9+ typical |
| **Backend** | FastAPI | Async; file upload via `UploadFile` |
| **Server** | Uvicorn | `uvicorn app:app --reload` |
| **Transcription** | OpenAI Whisper API | `whisper-1` |
| **Structuring** | OpenAI Chat Completions | `gpt-4o-mini` |
| **Frontend** | HTML + vanilla JS | No framework |
| **Config** | python-dotenv | Loads `.env` |

---

## Boundaries and Constraints

### In Scope (Demo)

- One-shot upload → transcribe → structure → display.
- Stateless: no database, no user accounts, no stored outputs.
- Local or single-host deployment (e.g. laptop + ngrok).

### Out of Scope (By Design)

- **Persistence:** No DB; temp file removed after each request.
- **Auth:** No login or API keys in frontend; backend uses server-side `OPENAI_API_KEY` only.
- **Scale:** No queues, workers, or horizontal scaling; single process.
- **Large files:** 25MB limit (Whisper); no chunked or resumable uploads.
- **Retries:** No automatic retry; user can re-upload.

### Security (Demo)

- API key only in `.env`; not committed (see `.gitignore`).
- No user data stored; no PII beyond what user uploads in the request.
- For public sharing (e.g. ngrok), treat as demo-only; no production guarantees.

---

## Deployment (Demo)

- **Local:** `cd demo && source .venv/bin/activate && uvicorn app:app --reload` → http://127.0.0.1:8000
- **Share:** e.g. `ngrok http 8000`; share the ngrok URL.
- **Production:** Not covered; see PRD and TECHNICAL_APPROACH for when to move to full architecture.

---

## Related Documents

- **[TECHNICAL_APPROACH.md](./TECHNICAL_APPROACH.md)** — Why Option B was chosen; trade-offs.
- **[CODE_MAPPING.md](./CODE_MAPPING.md)** — How this architecture maps to BMAD decisions.
- **[bmad-output/planning-artifacts/](./bmad-output/planning-artifacts/)** — Full PRD, product brief, demo technical approach.
