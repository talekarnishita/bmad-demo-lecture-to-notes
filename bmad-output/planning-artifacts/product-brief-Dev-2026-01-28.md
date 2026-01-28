---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments: []
date: 2026-01-28
author: Nishitatalekar
---

# Product Brief: Dev

<!-- Content will be appended sequentially through collaborative workflow steps -->

## Executive Summary

Students attend lectures but forget most of the material and struggle to turn notes into something useful. Current tools—transcription apps, note-taking apps, AI summarizers—don't connect recordings, notes, and summaries into a coherent learning structure. **Dev** is a learning-structure engine for university students, especially in technical subjects. Users upload a lecture and get structured notes, summaries, key concepts, concept maps, and auto-generated flashcards. Studying becomes review instead of re-learning; learning feels manageable instead of overwhelming. The product isn't summarization—it organizes by concepts, links related ideas across lectures, and turns passive recordings into an active study system.

---

## Core Vision

### Problem Statement

Students attend lectures but forget most of the material and struggle to turn notes into something useful. They take manual notes in notebooks, Notion, or Google Docs, rely on lecture recordings but rarely rewatch them fully, and sometimes use transcription tools like Otter—only to end up with long raw transcripts they don't revisit. Summarizing usually happens during exam prep, which turns into cramming. Current tools don't connect recordings, notes, and summaries well. There's no strong link between the recording, notes, and key concepts; it's hard to extract what actually matters.

### Problem Impact

Transcripts exist, but students still have to structure everything themselves. Notes don't help build a mental model—just scattered information. During exams, they waste time re-learning instead of reviewing. The result: poor retention, heavy cramming, lower confidence in technical subjects, and many avoiding difficult courses because learning feels overwhelming.

### Why Existing Solutions Fall Short

Tools like Otter, Notion, Obsidian, and generic AI summarizers give raw text, not learning structure. There's no hierarchy of concepts, no clear distinction between key ideas and supporting detail, and no strong connection between lecture audio and a knowledge map. They aren't designed for technical subjects where concepts build on each other. The main gap is **structured understanding**—concept hierarchy, key vs. supporting detail, and links between related topics across lectures.

### Proposed Solution

**Dev** lets students upload a lecture and instantly get structured notes, summaries, and key concepts. The core flow extends to concept maps or structured outlines, auto-generated flashcards, the ability to ask questions about the lecture, and linking concepts across multiple lectures. Studying becomes review instead of re-learning; stress drops and learning feels manageable instead of overwhelming.

### Key Differentiators

- **Learning structure engine, not summarization:** Organizes by concepts instead of sentences, understands technical content, and connects lectures over time.
- **From passive to active:** Turns passive recordings into an active study system—concept hierarchy, key vs. supporting detail, cross-lecture links.
- **Built for technical subjects:** Designed for dense, concept-heavy material where ideas build on each other.
- **Timing:** AI can now handle long lectures and structure meaning; students rely more on recordings than ever, but study tools haven't caught up. Growing stress and overload in education make this the right moment.

---

## Target Users

### Primary Users

**Aisha** — 2nd-year undergraduate, Computer Science. She takes four technical courses (Data Structures, Discrete Math, Systems, Linear Algebra). Lectures are dense, fast-paced, and often recorded. She attends class but can't capture everything while trying to understand.

- **Typical week:** Lectures during the day, assignments at night. Before exams or quizzes, she returns to slides, scattered notes, and sometimes recordings, spending a lot of time reconstructing what the lecture was about.
- **Where Dev fits:** After each lecture, she uploads the recording. Dev gives her structured notes, key concepts, and summaries. Before exams, she uses Dev to review concepts quickly instead of rewatching full lectures.
- **What she's trying to accomplish:** Truly understand concepts (not just copy notes), keep up with weekly material, and feel prepared for exams without last-minute cramming.

**Daniel** — 1st-year graduate student, Electrical Engineering. His courses are highly theoretical and build on each other. Professors assume prior knowledge and move quickly; lectures introduce complex ideas that connect across weeks.

- **Typical week:** Lectures, papers, and problem sets. He often revisits old notes to understand new material but struggles to remember how earlier concepts connect.
- **Where Dev fits:** Dev gives him structured breakdowns of each lecture and shows how concepts connect over time. He uses it to revisit foundational ideas when later material depends on them.
- **What he's trying to accomplish:** A clear conceptual map of the course so he can understand how ideas build, not just memorize steps.

### Secondary Users

- **Teaching Assistants (TAs):** May suggest tools to help students keep up; influence discovery and adoption.
- **Instructors:** Provide lecture recordings and may encourage structured review; influence adoption.
- **Universities or departments:** Could offer Dev as a learning support tool; influence discovery and adoption at scale.

Secondary users don't use the product the same way as students but influence how it's discovered and adopted.

### User Journey

- **Discovery:** Aisha or Daniel hear about Dev through classmates, student communities (Discord, Reddit, WhatsApp groups), or seeing someone use it while studying. Later, universities or TAs may recommend it.
- **Onboarding:** Sign up → upload a lecture recording (or paste a link) → Dev generates structured notes, summaries, and key concepts.
- **Aha moment:** The first time they study for a quiz or exam using Dev instead of rewatching lectures—they realize they understand the material faster and more clearly. Another "aha" is when a confusing concept clicks thanks to the structured breakdown or concept map.
- **Long-term use:** Dev becomes part of their routine after each lecture: upload → review structured notes, key concepts, and summaries. Before exams, they use Dev to review concepts quickly instead of rewatching full lectures.

---

## Success Metrics

### User Success

**Outcome users want:** Students want to understand lecture material faster, retain it better, and feel prepared for exams without rewatching long recordings or rebuilding notes from scratch.

**How they know it's working:** They can review a lecture in minutes instead of an hour, concepts feel clearer, and they feel more confident going into quizzes or exams.

**When they realize it's solving the problem:** The first time they prepare for an assessment using Dev and notice they don't need to rewatch lectures yet still understand the material. Another moment is when a previously confusing topic becomes clear through the structured notes or concept breakdown.

**Behaviors that show value:**
- Uploading lectures regularly after class
- Returning to Dev before exams to review summaries and key concepts
- Using generated flashcards or asking follow-up questions
- Spending less time rewatching lectures

**"This is working" if:** Students rely on Dev as part of their normal study workflow and feel it meaningfully reduces stress and improves understanding.

### Business Objectives

**3 months:**
- Early user adoption among students in technical courses
- Users repeatedly uploading lectures (not just one-time use)
- Strong engagement during exam periods
- Positive qualitative feedback (e.g. "this saves me so much time")

**12 months:**
- Consistent weekly active users during academic terms
- Growth through word-of-mouth among student communities
- Expansion across multiple courses and majors
- Potential partnerships or pilots with departments or universities

### Key Performance Indicators

- **Lectures uploaded per user** — measures depth of adoption and habit formation
- **Weekly active users (WAU)** — measures ongoing engagement during terms
- **Repeat usage before exams** — measures reliance on Dev for assessment prep
- **Retention over a semester** — measures whether Dev stays part of the study workflow
- **User-reported time saved or confidence improvement** — qualitative/UX metrics aligned with user success

---

## MVP Scope

### Core Features

**Core functionality that must work:** Students can upload a lecture recording and receive structured notes, a clear summary, and key concepts from that lecture.

**Features that directly solve the main problem:**
- Lecture upload (audio or video file)
- Automatic transcription and processing
- Structured notes with clear sections and hierarchy
- Short, high-level lecture summary
- Highlighted key concepts or definitions
- Simple interface to read and review outputs

**What would feel incomplete if missing:** If students only got raw transcripts or generic summaries without structure, the product wouldn't solve the core problem. Structured understanding is essential.

**What creates the "aha" moment:** The first time a student prepares for a quiz or exam using Dev's structured notes instead of rewatching the lecture, and realizes they understand the material faster and more clearly.

### Out of Scope for MVP

**Nice-to-have but not essential (explicitly deferred):**
- Concept maps or visual graphs
- Cross-lecture concept linking
- Auto-generated flashcards
- AI Q&A tutor / chat
- Collaboration or sharing
- LMS integrations
- Study planning features

We are explicitly saying "no" to these for MVP so we can focus on solving lecture → structured understanding really well.

### MVP Success Criteria

**We know the MVP works if:**
- Students upload lectures regularly, not just once
- They return to Dev before exams
- They spend less time rewatching lectures
- Qualitative feedback like "this saves me time" or "this made things click"

**Key signals:** Repeat uploads per user, weekly active users during term, and strong usage spikes before assessments.

### Future Vision

If successful, Dev evolves into a full learning-structure platform over 2–3 years:
- Linking concepts across lectures and courses
- Visual concept maps
- Flashcards and spaced repetition
- AI tutoring on lecture content
- Integration with universities or departments
- Expansion beyond technical subjects
