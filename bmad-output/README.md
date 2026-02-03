# BMAD Planning Artifacts

This directory contains the BMAD (product-development method) planning artifacts that document the thinking and decisions behind the Dev demo implementation.

## What is BMAD?

BMAD makes product thinking and decisions **explicit and reviewable**. It's not just about building code—it's about documenting *why* decisions were made, not just *what* was built.

## Artifacts

### Planning Documents

- **[product-brief-Dev-2026-01-28.md](./planning-artifacts/product-brief-Dev-2026-01-28.md)** — Problem statement, target users, success metrics, and MVP scope
- **[prd.md](./planning-artifacts/prd.md)** — Full Product Requirements Document with success criteria, user journeys, functional requirements, and non-functional requirements
- **[demo-technical-approach.md](./planning-artifacts/demo-technical-approach.md)** — Technical architecture decisions, trade-offs, and why Option B (web app) was chosen

### Root-Level Summaries

For quick reference, concise versions and architecture are available in the repo root:

- **[PRODUCT_BRIEF.md](../PRODUCT_BRIEF.md)** — Concise problem, user, goal
- **[PRD.md](../PRD.md)** — Demo scope, success criteria, constraints
- **[TECHNICAL_APPROACH.md](../TECHNICAL_APPROACH.md)** — Architecture decisions and trade-offs
- **[architecture.md](../architecture.md)** — System architecture: components, data flow, stack, repo structure
- **[CODE_MAPPING.md](../CODE_MAPPING.md)** — How code implements the decisions

## Why These Matter

These artifacts allow reviewers to:

- **Understand the problem** — Why was this built?
- **See the reasoning** — Why was Option B chosen over CLI or notebook?
- **Review trade-offs** — What was deferred and why?
- **Trace decisions** — How do PRD requirements map to code?

This makes the work **reviewable, reusable, and scalable**—you can see the thinking behind the code, not just the code itself.

## BMAD Workflow

The artifacts follow BMAD's structured workflow:

1. **Product Brief** — Problem, user, goal, success criteria
2. **PRD** — Detailed requirements, scope, user journeys, functional/non-functional requirements
3. **Technical Approach** — Architecture decisions, trade-offs, implementation choices
4. **Code Mapping** — How code implements the decisions above

Each artifact builds on the previous one, creating a traceable chain from problem → solution → implementation.
