# PRD: Dev Demo

**Date:** 2026-01-28  
**Author:** Nishitatalekar

## Product Scope

### MVP — Minimum Viable Product (Demo)

**Core functionality:**
- Lecture upload (audio or video file)
- Automatic transcription and processing
- Structured notes with clear sections and hierarchy
- Short, high-level lecture summary
- Highlighted key concepts or definitions
- Simple interface to read and review outputs

**What makes MVP complete:**
- Students can upload a lecture and receive structured notes, a clear summary, and key concepts
- Outputs are accurate and understandable without rechecking audio
- Processing completes within 2–5 minutes for a typical lecture

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

### Out of Scope for Demo

**Explicitly deferred (not building):**
- User accounts, auth, sessions
- Database or persistence (stateless, request-scoped only)
- Production infrastructure (scaling, monitoring, CI/CD)
- Error retry logic beyond basic messages
- Cross-lecture features, concept maps, flashcards, Q&A
- LMS integrations or institutional features

**Why:** This is a demo to validate output quality, not a production system. Focus on core value (structured notes) before investing in infrastructure.

### Growth Features (Post-Demo)

**Future capabilities (not in demo):**
- Concept maps or visual graphs
- Cross-lecture concept linking
- Auto-generated flashcards
- AI Q&A tutor / chat on lecture content
- User accounts and persistence
- Production infrastructure

## Success Criteria

### User Success

**Review efficiency:**
- Students review the key material from a 60–90 minute lecture in **5–10 minutes** using Dev's structured notes and summary
- This represents **70–80% time savings** compared to rewatching the full lecture

**Clarity and confidence:**
- Students report that concepts feel clearer after using Dev
- Students feel more confident going into quizzes and exams

**Behavioral indicators:**
- Users understand the output without confusion
- Users want to use it again (positive qualitative feedback)
- Users report that concepts feel clearer

### Output Quality

**Structure quality:**
- Structured notes are clear and logically organized
- Summary captures main ideas accurately
- Key concepts are relevant and well-identified
- Output format matches specification (sections, summary, keyConcepts)

**Transcription quality:**
- Transcription accuracy high enough that notes are understandable without rechecking the audio
- Handles common audio/video formats (mp3, mp4, m4a, wav, webm)

### Technical Success

**Processing time:**
- Outputs (structured notes, summary, key concepts) generated within **2–5 minutes** for a typical 60-minute lecture

**Reliability:**
- System works consistently without frequent failures
- Very low rate of failed processing or corrupted outputs
- Clear error messages when processing fails

**Constraints:**
- File size limit: 25MB (Whisper API constraint)
- Stateless: No sessions, no stored data
- No persistence: Each request is independent

### Measurable Outcomes

| Metric | Target |
|--------|--------|
| Review time for 60–90 min lecture | 5–10 minutes |
| Time savings vs. rewatching | 70–80% |
| Processing time (60 min lecture) | 2–5 minutes |
| File size limit | 25MB max |
| Output quality | Clear, organized, understandable |

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
