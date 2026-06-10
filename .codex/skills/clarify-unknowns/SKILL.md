---
name: clarify-unknowns
description: Resolve unknowns in intent, feature, product brief, requirements, or specification documents by inspecting the artifact, asking focused clarification questions, and updating the source description so resolved unknowns are captured. Use when a user asks to clarify unknowns, remove open questions, resolve ambiguity, make a feature intent implementation-ready, or update a feature description after answering questions.
---

# Clarify Unknowns

## Purpose

Use this skill to turn unresolved product or feature ambiguity into durable
intent text without inventing business rules.

## Workflow

1. Locate the target artifact.
   - Prefer the file the user named.
   - If no file is named, inspect likely intent or feature directories such as
     `1_intent/`, `intent/`, `features/`, `docs/`, or `specs/`.
   - If multiple plausible targets exist, ask which one to update before
     editing.

2. Read the surrounding methodology and expectations.
   - In ICE repositories, read the local methodology or agent instructions
     before changing intent files.
   - Preserve the repository's separation of durable intent from lifecycle
     tracking. Do not add proposal status, implementation status, or completion
     notes to intent artifacts.

3. Identify unknowns.
   - Look for explicit sections named `Unknowns`, `Open Questions`, `TBD`,
     `Assumptions`, `Risks`, or inline uncertainty.
   - Distinguish answerable clarification questions from implementation
     choices an agent can decide later.
   - Do not ask about details that are already answered elsewhere in the
     artifact or nearby context.

4. Ask focused questions.
   - Batch related questions, but keep the list short enough for the user to
     answer directly.
   - Prefer concrete choices when the document implies clear options.
   - Include a free-form path when the options may be incomplete.
   - Ask only questions whose answers will change the durable feature
     description.

5. Update the feature description.
   - Incorporate answers into the most relevant durable sections, such as
     `Desired Outcome`, `User Impact`, `Anti-Goals`, `Assumptions`, or feature
     constraints.
   - Remove a resolved item from `Unknowns` or `Open Questions`.
   - If an answer is partial, replace the old unknown with a narrower remaining
     unknown instead of deleting it.
   - If the user declines to decide, preserve the unknown and document any
     explicit default or non-decision as an assumption only if the user stated
     it.

6. Validate the result.
   - Re-read the changed artifact and confirm there are no stale contradictions.
   - Check that all resolved unknowns appear as durable product intent,
     constraints, assumptions, or anti-goals.
   - Confirm that remaining unknowns are still genuinely unresolved.

7. Report succinctly.
   - Summarize what was resolved and what remains.
   - Name the file updated.
   - Do not claim there are no unknowns if any uncertainty remains in the
     artifact.

## Question Quality

Use questions that reduce ambiguity without steering the product decision.

Good:

```text
Should daily open hours allow one continuous window per day, or multiple
windows for breaks and split sessions?
```

Poor:

```text
Should I implement this with a normalized hours table?
```

Good:

```text
After a convention is created, which fields may organizers edit before the
event starts?
```

Poor:

```text
Should editing be CRUD?
```

## Editing Rules

- Preserve the author's voice and the document's existing structure.
- Prefer small targeted edits over rewriting the whole document.
- Do not invent requirements, business rules, edge cases, or policy.
- Do not move unresolved decisions into acceptance criteria.
- Do not remove anti-goals unless the user explicitly changes scope.
- Keep dates, owners, and metadata current only when the repository convention
  requires it.
