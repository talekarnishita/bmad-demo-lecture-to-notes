# Dev Demo — Minimal Technical Approach

**Purpose:** Validate output quality (transcription → structured notes) with real users before architecture and full implementation.  
**Scope:** Upload → transcription → structured notes using AI. No auth, no database, no production infra.

---

## 1. Demo Scope

**In scope:**
- User uploads a lecture recording (audio or video file).
- System transcribes the recording (third-party API).
- System produces structured notes: **sections**, **short summary**, **key concepts** (LLM).
- User sees "Processing…" then the structured output in a simple UI or via exported file.

**Out of scope (for demo):**
- User accounts, auth, or sessions.
- Storing lectures or outputs (no database; request-scoped only).
- Production infrastructure (scaling, monitoring, CI/CD, etc.).
- Retry/error UX beyond a simple message; no support dashboard.
- Cross-lecture linking, concept maps, flashcards, or Q&A.

---

## 2. High-Level Flow

```
[User] → upload file → [Demo app] → transcribe (API) → structure (LLM) → [User] sees result
```

- **Stateless:** Each run = one upload, one transcript, one structured output. Nothing persisted.
- **Local or single-endpoint:** Run on your machine, or one serverless function / minimal app for sharing.

---

## 3. Minimal Architecture Options

### Option A: Local CLI (fastest to build)

**Idea:** A small script (Python or Node) that takes a file path, calls transcription + LLM, and writes structured notes to disk (or stdout).

**Flow:**
1. `python demo_dev.py path/to/lecture.mp4`
2. Script uploads file to transcription API (e.g. Whisper), gets transcript.
3. Script sends transcript to LLM with a fixed "structure" prompt → sections, summary, key concepts.
4. Script writes Markdown (or JSON) to `./output/lecture-name.md`.

**Pros:** Almost zero infra, quick to iterate on prompts, easy to run on real lectures.  
**Cons:** No browser UX; test users need to run it locally or you run it for them and share outputs.

**Best for:** Solo validation of output quality and prompt design before any UI.

---

### Option B: Minimal web app (best for user testing)

**Idea:** One HTML page + a tiny backend (or single serverless function). User drops a file, sees "Processing…", then structured notes in the browser.

**Frontend:**
- Single page: file input (or drag-and-drop), "Processing…" state, then rendered result (sections, summary, key concepts).
- No routing, no framework required; vanilla JS or a minimal SPA is enough.

**Backend:**
- One HTTP endpoint (e.g. `POST /process`): accepts `multipart/form-data` file.
- In memory (or temp dir): save upload → call transcription API → call LLM with structure prompt → return JSON (or HTML) → discard temp file.
- No auth, no DB. Optional: rate limit by IP or a shared demo secret if you expose it.

**Hosting (demo-only):**
- **Local:** Run backend (e.g. FastAPI, Express) on your machine; share via ngrok (or similar) so users hit your laptop.
- **Static + serverless:** Frontend on Vercel/Netlify; one serverless function (e.g. Vercel serverless, Netlify function) that does transcribe + structure. Still no DB, no prod infra.

**Pros:** Real "upload → see result" experience; easy to hand to a few users for feedback.  
**Cons:** Slightly more than a CLI; you manage one backend or serverless endpoint.

**Best for:** Validating output quality **with** real users in a product-like flow.

---

### Option C: Jupyter / Colab notebook

**Idea:** Step-by-step cells: upload file → transcribe → structure → display. Good for prompt iteration and trying different lectures.

**Pros:** Fast to change prompts and re-run; shareable via Colab link.  
**Cons:** Not a "product" experience; less natural for non-technical test users.

**Best for:** Experimenting with structure prompts and model choices before locking the demo.

---

## 4. Recommended Path: Option B (minimal web app)

**Why:** You want to validate with **real users**. A small web app gives you upload → processing → result without auth/DB/infra, and you can run it locally or behind a single serverless endpoint.

**Stack sketch:**

| Layer | Choice | Notes |
|-------|--------|-------|
| **Frontend** | Single HTML + JS, or minimal React/Vue | File input, "Processing…", render sections / summary / key concepts |
| **Backend** | FastAPI (Python) or Express (Node) — or one serverless function | Single `POST /process`; temp file → transcribe → structure → respond |
| **Transcription** | OpenAI Whisper API, or AssemblyAI, or Deepgram | All support file upload + transcript; pick one and stick with it for demo |
| **Structuring** | OpenAI API (GPT-4 or GPT-4o) or Claude, etc. | One prompt: transcript → structured JSON (sections, summary, key concepts) |
| **Hosting** | Local + ngrok, or Vercel/Netlify serverless | No DB, no production services |

**Output format (align with PRD):**

- **Sections:** Array of `{ "heading": "...", "content": "..." }`.
- **Summary:** Single string (short, high-level).
- **Key concepts:** Array of strings or `{ "term": "...", "definition": "..." }`.

Return as JSON; frontend renders as simple sections + summary + concepts.

---

## 5. Implementation Checklist (minimal)

**Backend (single `POST /process`):**
- [ ] Accept `multipart` upload; support typical audio/video formats (e.g. mp4, mp3, m4a, webm).
- [ ] Optional: max file size (e.g. 100–200 MB) to avoid timeouts.
- [ ] Write to temp file (or in-memory buffer if provider allows).
- [ ] Call transcription API; handle errors with a simple message (e.g. "Transcription failed").
- [ ] Call LLM with structure prompt; parse response into sections, summary, key concepts.
- [ ] Return JSON (and/or serve a simple HTML view).
- [ ] Delete temp file; no persistence.

**Frontend:**
- [ ] File input (and optional drag-and-drop).
- [ ] "Processing…" state; optional simple progress (e.g. "Transcribing…" → "Structuring…") if you have two clear steps.
- [ ] Render sections, summary, key concepts (heading hierarchy, bullets).
- [ ] Optional: "Copy" or "Download as Markdown" for sharing.

**APIs:**
- [ ] Pick transcription provider; add API key (env var or config).
- [ ] Pick LLM provider; add API key.
- [ ] Ensure prompt (and, if needed, response format) matches your structure (sections, summary, key concepts).

**Running the demo:**
- [ ] Local: run backend + frontend; use ngrok (or similar) to share.
- [ ] Or: deploy frontend + one serverless route; keep it explicitly demo, not production.

---

## 6. What You're Validating

- **Transcription quality:** Accuracy, readability for typical lecture audio.
- **Structure quality:** Do sections, summary, and key concepts match what users expect? Does it feel like "review in minutes"?
- **Rough timing:** How long does a typical 30–60 min lecture take end-to-end? (No SLA; just feedback.)

**Lightweight feedback:** After showing the result, you can add a simple "Was this useful? Quick comment?" text field or link to a form (e.g. Typeform, Google Form) — still no auth or DB.

---

## 7. Explicit Non-Goals for Demo

- No user accounts, login, or sessions.
- No database or persistence of lectures/outputs.
- No production-grade security, scaling, or monitoring.
- No retry queue, job workers, or multipart upload for very large files; keep it single-request.
- No LMS, auth, or FERPA considerations; treat as internal/invited-user demo only.

---

## 8. Implementation (Option B)

A minimal Option B implementation lives in **`demo/`**:

- **`demo/app.py`** — FastAPI app: `GET /` serves the UI, `POST /process` accepts upload → Whisper → GPT structure → JSON.
- **`demo/static/index.html`** — Single page: file input + drag-and-drop, "Processing…", render sections/summary/key concepts, Download as Markdown, Copy, Process another.
- **`demo/requirements.txt`** — fastapi, uvicorn, python-multipart, openai, python-dotenv.
- **`demo/.env.example`** — `OPENAI_API_KEY` (required). Optional `MAX_UPLOAD_BYTES` (default 25MB).
- **`demo/README.md`** — Run locally (`uvicorn app:app --reload`), ngrok for sharing.

**Run:** `cd demo && pip install -r requirements.txt && cp .env.example .env` (set `OPENAI_API_KEY`), then `uvicorn app:app --reload` → http://127.0.0.1:8000.

---

## 9. When to Move Back to Full Build

Resume architecture and full implementation when:

- You're satisfied with output quality (transcription + structure) from real lectures and user feedback.
- You're ready to add auth, persistence, and production infra per the PRD.

Until then, this demo remains the minimal technical approach to validate **output quality** with real users.
