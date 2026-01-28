# Dev — Demo

Minimal web app to validate **output quality** (transcription → structured notes) with real users. No auth, no database, no production infra.

**Flow:** Upload lecture (audio/video) → transcribe (Whisper) → structure (GPT) → show sections, summary, key concepts.

---

## BMAD and this code

This demo was specified and built using **BMAD** (a product-development method: product brief → PRD → technical approach → implementation). Understanding that flow helps you see how the code matches the spec.

### How BMAD was used

1. **Product brief** — Defined Dev as a learning-structure engine for students: upload a lecture → get structured notes, summary, key concepts. Target: “review in minutes, not rewatching.”
2. **PRD** — Captured success criteria, user journeys, and MVP scope (web app, upload → process → structured review).
3. **Demo technical approach** — Chose a minimal path to validate output quality *before* full architecture: Option A (CLI), Option B (web app), Option C (notebook). **Option B** was chosen for real user testing.
4. **This repo** — Implementation of Option B: one backend endpoint, one frontend page, no auth or DB.

### How the code maps to the spec

| Spec (from BMAD) | Code |
|------------------|------|
| User uploads lecture (audio/video) | `static/index.html` — file input + drag-and-drop; `POST /process` in `app.py` |
| Transcribe → structure (sections, summary, key concepts) | `app.py`: Whisper API → transcript, then GPT with `STRUCTURE_PROMPT` → JSON |
| Output format: sections, summary, keyConcepts | Same shape in `app.py` response and in the UI render in `static/index.html` |
| No auth, no DB, stateless | No sessions or storage; temp file deleted after request |
| Demo-only hosting | Run locally or expose via ngrok (see below) |

So: **BMAD defined *what* to build and *why*; this code is the *how* for the demo.** When you change prompts, add UI, or tweak the flow, you’re iterating on the same scope (output quality, single-request flow) that BMAD locked in for the demo.

If this repo lives inside a larger Dev repo, BMAD artifacts live in **`_bmad-output/planning-artifacts/`** (e.g. `prd.md`, `demo-technical-approach.md`). If you only have this `demo/` folder, the table above is the bridge from “BMAD spec” to “this code.”

---

## Run locally

1. **Setup**

   ```bash
   cd demo
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Config**

   Put your API key in `.env` (never committed — it’s in `.gitignore`):

   ```bash
   cp .env.example .env
   # Edit .env and set OPENAI_API_KEY=sk-...
   ```

3. **Start**

   ```bash
   uvicorn app:app --reload
   ```
   Or: `python3 -m uvicorn app:app --reload` if `uvicorn` isn’t on your PATH.

   Open **http://127.0.0.1:8000** → upload a file → see structured notes.

---

## Share with others (e.g. ngrok)

```bash
ngrok http 8000
```

Give users the ngrok URL. They upload, get results; no sign-up. Treat as demo-only (no auth, no persistence).

---

## Limits

- **File size:** 25MB (Whisper API). For longer lectures, use shorter clips or another transcription provider later.
- **Formats:** mp3, mp4, mpeg, mpga, m4a, wav, webm.

---

## Optional

- **Feedback:** Add a “Was this useful?” link to a Typeform/Google Form; no backend changes.
- **`MAX_UPLOAD_BYTES`** in `.env` — keep ≤ 25MB for Whisper.
