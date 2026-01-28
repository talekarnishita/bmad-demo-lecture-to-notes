# PRD: Dev Demo

**Date:** 2026-01-28  
**Author:** Nishitatalekar

## Scope

### In Scope

**Core flow:**
1. User uploads lecture recording (audio/video)
2. System transcribes using Whisper API
3. System structures transcript into: sections, summary, key concepts
4. User views structured output in browser

**Output format:**
- **Sections:** Array of `{heading, content}` with logical hierarchy
- **Summary:** Short paragraph (2–4 sentences) capturing main ideas
- **Key concepts:** Array of important terms/ideas, optionally with definitions

**UI:**
- File upload (drag-and-drop)
- "Processing…" state
- Rendered structured output
- Optional: download as Markdown

### Out of Scope

- User accounts, auth, sessions
- Database or persistence (stateless, request-scoped only)
- Production infrastructure (scaling, monitoring, CI/CD)
- Error retry logic beyond basic messages
- Cross-lecture features, concept maps, flashcards, Q&A

**Why:** This is a demo to validate output quality, not a production system.

## Success Criteria

### Output Quality
- Structured notes are clear and logically organized
- Summary captures main ideas accurately
- Key concepts are relevant and well-identified
- Users can review a 60–90 min lecture in 5–10 minutes

### User Validation
- Users understand the output without confusion
- Users report that concepts feel clearer
- Users want to use it again (positive qualitative feedback)

### Technical
- Processing completes within reasonable time (2–5 min for 60 min lecture)
- Handles common audio/video formats (mp3, mp4, m4a, wav, webm)
- File size limit: 25MB (Whisper API constraint)

## Constraints

- **No persistence:** Each request is independent
- **No auth:** Demo-only, shared via ngrok or similar
- **File size:** 25MB max (Whisper API limit)
- **Stateless:** No sessions, no stored data

## Non-Goals

Explicitly **not** building:
- User accounts or authentication
- Database or data persistence
- Production-grade security or scaling
- Advanced features (concept maps, flashcards, Q&A)
- LMS integrations or institutional features

**Rationale:** Validate core value (structured notes) before investing in infrastructure.
