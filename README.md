# Dev — Demo

Minimal web app to validate **output quality** (transcription → structured notes) with real users. No auth, no database, no production infra.

**Flow:** Upload lecture (audio/video) → transcribe (Whisper) → structure (GPT) → show sections, summary, key concepts.

---

## BMAD Planning Artifacts

This demo was built using **BMAD** (a product-development method that makes thinking and decisions explicit and reviewable). The planning artifacts document *why* decisions were made, not just *what* was built.

### Full BMAD Artifacts

Complete planning documents are in **[`bmad-output/planning-artifacts/`](./bmad-output/planning-artifacts/)**:

- **[product-brief-Dev-2026-01-28.md](./bmad-output/planning-artifacts/product-brief-Dev-2026-01-28.md)** — Full product brief with problem, users, success metrics, MVP scope
- **[prd.md](./bmad-output/planning-artifacts/prd.md)** — Complete PRD with success criteria, user journeys, functional/non-functional requirements
- **[demo-technical-approach.md](./bmad-output/planning-artifacts/demo-technical-approach.md)** — Detailed technical approach with architecture options and decisions

See **[`bmad-output/README.md`](./bmad-output/README.md)** for an overview of the BMAD workflow.

### Quick Reference (Root Level)

Concise summaries and architecture:

- **[PRODUCT_BRIEF.md](./PRODUCT_BRIEF.md)** — Problem, user, goal, success criteria
- **[PRD.md](./PRD.md)** — Scope, success criteria, constraints, and non-goals
- **[TECHNICAL_APPROACH.md](./TECHNICAL_APPROACH.md)** — Architecture decisions and trade-offs
- **[architecture.md](./architecture.md)** — System architecture: components, data flow, stack, repo structure
- **[CODE_MAPPING.md](./CODE_MAPPING.md)** — How code implements the decisions above

### Why These Matter

BMAD isn't just about building code—it's about making the **reasoning** visible:
- **Product Brief** explains the problem and why this solution matters
- **PRD** defines what's in scope and what's explicitly deferred (with detailed success criteria)
- **Technical Approach** documents why Option B (web app) was chosen over CLI or notebook
- **Code Mapping** shows how each decision maps to actual code

**Review these artifacts** to understand:
- Why we chose a minimal web app instead of full architecture
- Why there's no auth, database, or persistence
- Why the output format is sections + summary + key concepts
- What trade-offs were made and why they're acceptable for a demo

This makes the work **reviewable, reusable, and scalable**—you can see the thinking behind the code, not just the code itself.

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
