# Completion Report

## Metadata

- Work Item: patterns-template-scope-guidance
- Owner: Codex
- Completion Date: 2026-06-10
- Proposal: `work/1_proposed/patterns-template-scope-guidance.md`
- Intent: `1_intent/product.md`

## Outcome

Updated `2_context/_patterns-template.md` with scope guidance that distinguishes
architecture context from pattern context and recommends scoped pattern files
when guidance is area-specific.

## Expectations Validation

### Engineering

PASS

The change preserves the existing template, adds concise guidance, and aligns
with the methodology's distinction between architecture and existing patterns.

### Testing

PASS

No automated tests apply to this documentation-only change. The updated template
was inspected directly.

### Security

PASS

No security-sensitive behavior or configuration changed.

## Discoveries

- `2_context/idsd_methodology.md` already treats architecture and existing
  patterns as separate context categories.
- `work/1_proposed/_proposed_feature-template.md` asks proposals to reference
  architecture, constraints, ADRs, and patterns separately.

## Context Updates Recommended

- Applied in `2_context/_patterns-template.md`.

## Follow-Up Work

- None.
