# Technical Approach: Dev Demo

**Date:** 2026-01-28  
**Author:** Nishitatalekar

## Why This Approach

**Goal:** Validate output quality (transcription → structured notes) with real users before building full architecture.

**Decision:** Build a minimal web app (Option B) instead of CLI or notebook.

**Rationale:**
- **CLI (Option A)** is fastest but requires users to run commands → not realistic for testing
- **Notebook (Option C)** is good for iteration but not a product-like experience
- **Web app (Option B)** gives real "upload → see result" flow → best for user validation

## Architecture Choice

### Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Backend** | FastAPI (Python) | Simple, fast to build, handles file uploads well |
| **Frontend** | Single HTML + vanilla JS | No framework needed; minimal complexity |
| **Transcription** | OpenAI Whisper API | High accuracy, easy integration, handles common formats |
| **Structuring** | OpenAI GPT-4o-mini | Good balance of quality and cost for demo |
| **Hosting** | Local + ngrok | No infrastructure needed; easy to share |

### Flow

```
User → upload file → FastAPI endpoint → Whisper API → GPT prompt → structured JSON → UI render
```

**Key decisions:**
- **Stateless:** No database; temp file deleted after request
- **Single endpoint:** `POST /process` handles everything
- **In-memory processing:** File → temp → API calls → response → cleanup
- **No auth:** Demo-only; share via ngrok

## Why Not Full Architecture?

**Deferred:**
- User accounts and authentication
- Database for storing lectures/outputs
- Production infrastructure (scaling, monitoring)
- Retry queues or job workers
- Multi-part uploads for large files

**Reason:** Validate output quality first. If structured notes work, then invest in infrastructure.

## Trade-offs

**Pros:**
- Fast to build and iterate
- Easy to test with real users
- No infrastructure costs
- Can validate core value quickly

**Cons:**
- No persistence (can't save outputs)
- No user accounts (can't track usage)
- Limited to 25MB files (Whisper constraint)
- Not production-ready

**Acceptable for demo:** These limitations are intentional to focus on output quality validation.

## When to Move Forward

Resume full architecture when:
- Output quality is validated with real users
- Users want to save outputs and return to them
- Ready to add auth, persistence, and production infrastructure

Until then, this minimal approach is sufficient.
