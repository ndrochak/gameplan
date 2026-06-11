# Proposed Work

## Metadata

- Work Item: patterns-template-scope-guidance
- Owner: Codex
- Date: 2026-06-10
- Status: completed
- Completion Report: `work/2_completed/20260610-006-patterns-template-scope-guidance.md`

## Intent Reference

- `1_intent/product.md`

## Intent Delta (Optional)

Clarify repository context authoring guidance so future agents can distinguish
architecture context from preferred engineering patterns.

## Relevant Context

- `2_context/idsd_methodology.md`: Context includes both system architecture
  and existing patterns, and overlapping artifacts should keep full detail in
  the primary artifact and link from secondary artifacts.
- `2_context/architecture.md`: Architecture context describes system shape,
  boundaries, integrations, and architecture-level patterns.
- `2_context/_patterns-template.md`: Template for documenting repeatable
  engineering patterns.

## Expectations

- `3_expectations/engineering.md`: Maintain consistency with existing patterns
  and avoid unnecessary structure.

## Proposed Approach

Update `2_context/_patterns-template.md` with scope guidance that distinguishes
architecture from patterns and recommends scoped pattern files when useful.

## Risks

- Too much guidance in a template could make future context docs verbose.
  Mitigation: keep the addition concise and directive.

## Questions

- None. The requested change is clear and narrow.
