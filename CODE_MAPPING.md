# Code Mapping: How Implementation Maps to Decisions

**Date:** 2026-01-28  
**Author:** Nishitatalekar

This document explains how the code implements the decisions made in the Product Brief, PRD, and Technical Approach.

## Decision → Code Mapping

### 1. Stateless, No Persistence

**Decision (PRD):** No database; each request is independent.

**Code:**
- `app.py`: Temp file created, processed, then deleted in `finally` block (lines 85-131)
- No database imports or models
- No session management

**Why:** Validates output quality without infrastructure complexity.

---

### 2. Single Endpoint Architecture

**Decision (Technical Approach):** One `POST /process` endpoint handles everything.

**Code:**
- `app.py`: Single `@app.post("/process")` function (lines 57-131)
- Handles: file upload → transcription → structuring → response
- No routing or multiple endpoints

**Why:** Simplest possible flow for demo validation.

---

### 3. Output Format: Sections, Summary, Key Concepts

**Decision (PRD):** Structured output with three components.

**Code:**
- `app.py`: `STRUCTURE_PROMPT` defines exact format (lines 25-38)
- Response validation checks for `summary`, `sections`, `keyConcepts` (line 116)
- `static/index.html`: Renders all three components in UI

**Why:** Matches PRD specification exactly; validates structured learning approach.

---

### 4. File Size Limit (25MB)

**Decision (PRD):** 25MB max due to Whisper API constraint.

**Code:**
- `app.py`: `MAX_UPLOAD_BYTES` env var, default 25MB (line 23)
- File size check before processing (lines 69-74)
- Error message explains limit

**Why:** Whisper API constraint; prevents API errors and timeouts.

---

### 5. No Authentication

**Decision (PRD):** Demo-only; no auth needed.

**Code:**
- No auth middleware or decorators
- No user session handling
- No login/logout endpoints

**Why:** Simplifies demo; focus on output quality, not security.

---

### 6. Processing Flow: Upload → Transcribe → Structure

**Decision (Technical Approach):** Sequential API calls: Whisper → GPT.

**Code:**
- `app.py`: Lines 90-95 (Whisper transcription)
- Lines 100-105 (GPT structuring with `STRUCTURE_PROMPT`)
- Error handling at each step

**Why:** Validates each step independently; easy to debug.

---

### 7. Frontend: Single Page, No Framework

**Decision (Technical Approach):** Minimal HTML + vanilla JS.

**Code:**
- `static/index.html`: Single file, no React/Vue
- Vanilla JavaScript for file upload and rendering
- Inline styles (no separate CSS)

**Why:** Fastest to build; no build step or dependencies.

---

### 8. Error Handling: Basic Messages

**Decision (PRD):** No retry logic; simple error messages.

**Code:**
- `app.py`: HTTPException with simple messages (lines 63-66, 71-74, 79-81, etc.)
- Frontend: Basic error display in UI
- No retry queue or complex error recovery

**Why:** Demo scope; sufficient for validation.

---

## Key Design Patterns

### Stateless Processing
- Each request is independent
- No shared state between requests
- Temp files cleaned up immediately

### API-First Backend
- Backend returns JSON
- Frontend handles rendering
- Easy to test backend independently

### Environment-Based Configuration
- `.env` for API keys (never committed)
- `.env.example` shows required variables
- `.gitignore` protects secrets

## What's Missing (By Design)

These are **intentionally** not implemented per PRD:

- **Database:** No persistence layer
- **Auth:** No user accounts
- **Sessions:** No state management
- **Retry logic:** No job queues
- **Production infra:** No scaling/monitoring

**Why:** This is a demo to validate output quality. Full architecture comes after validation.

## Future Mapping

When moving to full architecture, these decisions will change:

| Current (Demo) | Future (Production) |
|----------------|-------------------|
| Stateless | Database + sessions |
| Single endpoint | Multiple endpoints + routing |
| Temp files | Persistent storage |
| No auth | User accounts + auth |
| Local/ngrok | Production hosting |

But the core flow (upload → transcribe → structure) remains the same.
