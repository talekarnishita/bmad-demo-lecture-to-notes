"""
Dev demo — Option B: minimal web app.
Upload → transcribe (Whisper) → structure (GPT) → return JSON.
No auth, no DB, no persistence. Stateless.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MAX_UPLOAD_BYTES = int(os.getenv("MAX_UPLOAD_BYTES", "25_000_000").replace("_", ""))

STRUCTURE_PROMPT = """You are helping turn a raw lecture transcript into structured study notes for university students.

Given the transcript below, produce:
1. **summary**: A short, high-level paragraph (2–4 sentences) capturing the main ideas.
2. **sections**: An array of logical sections. Each has "heading" (brief title) and "content" (concise bullets or short paragraphs). Preserve meaningful hierarchy (intro, main topics, wrap-up).
3. **keyConcepts**: An array of important terms or ideas. Each can be a string, or {"term": "...", "definition": "..."} if a brief definition helps.

Return valid JSON only, no markdown or extra text. Use this exact structure:
{"summary": "...", "sections": [{"heading": "...", "content": "..."}, ...], "keyConcepts": [...]}

Transcript:
---
{transcript}
---"""

app = FastAPI(title="Dev Demo", description="Upload → transcribe → structured notes")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

static_dir = Path(__file__).resolve().parent / "static"
if static_dir.is_dir():
    app.mount("/static", StaticFiles(directory=str(static_dir), html=True), name="static")


@app.get("/")
async def index():
    """Serve the demo UI."""
    index_html = static_dir / "index.html"
    if not index_html.exists():
        raise HTTPException(status_code=404, detail="static/index.html not found")
    return FileResponse(index_html)


@app.post("/process")
async def process(file: UploadFile = File(...)):
    """
    Accept audio/video upload → transcribe with Whisper → structure with GPT → return JSON.
    """
    if not client:
        raise HTTPException(
            status_code=503,
            detail="OPENAI_API_KEY not set. Add it to .env and restart.",
        )

    # Enforce Whisper-friendly size (25MB)
    raw = await file.read()
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Max {MAX_UPLOAD_BYTES // 1_000_000}MB (Whisper limit).",
        )

    suffix = Path(file.filename or "audio").suffix or ".bin"
    if suffix not in {".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".wav", ".webm"}:
        raise HTTPException(
            status_code=400,
            detail="Unsupported format. Use mp3, mp4, m4a, wav, or webm.",
        )

    tmp = None
    try:
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
            f.write(raw)
            tmp = f.name

        # Transcribe
        with open(tmp, "rb") as audio:
            transcript_resp = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
            )
        transcript = transcript_resp.text.strip()
        if not transcript:
            raise HTTPException(status_code=422, detail="Transcription produced no text.")

        # Structure
        prompt = STRUCTURE_PROMPT.format(transcript=transcript)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        text = (completion.choices[0].message.content or "").strip()
        # Strip potential markdown code fences
        if text.startswith("```"):
            lines = text.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines)

        structured = json.loads(text)
        if "summary" not in structured or "sections" not in structured or "keyConcepts" not in structured:
            raise HTTPException(status_code=502, detail="LLM output missing summary/sections/keyConcepts.")

        return JSONResponse(content=structured)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=502, detail=f"LLM did not return valid JSON: {e}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if tmp and os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass
