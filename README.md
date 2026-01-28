# Dev — Demo (Option B)

Minimal web app to validate **output quality** (transcription → structured notes) with real users. No auth, no database, no production infra.

**Flow:** Upload lecture (audio/video) → transcribe (Whisper) → structure (GPT) → show sections, summary, key concepts.

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
