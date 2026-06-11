# Proposed Work

## Metadata

- Work Item: Work File Naming Order Convention
- Owner: Product
- Date: 2026-06-10
- Status: completed
- Approval Evidence: approved by human in chat on 2026-06-10 with instruction
  to order by historical git history
- Completion Report: `work/2_completed/20260610-016-work-file-naming-order-convention.md`

## Intent Reference

- `1_intent/product.md`

## Intent Delta (Optional)

Make work artifact ordering obvious from filenames by adopting a sortable naming
pattern that includes date and sequence.

## Relevant Context

- `AGENTS.md`: work items are tracked under `work/1_proposed/` and
  `work/2_completed/` and must preserve proposal-to-completion traceability.
- `2_context/idsd_methodology.md`: proposal and completion artifacts are
  lifecycle records and should remain easy to navigate.
- `work/1_proposed/_proposed_feature-template.md`: proposals are required before
  implementation and need explicit human approval.

## Expectations

- `3_expectations/engineering.md`: keep workflow changes simple and consistent
  with existing repository practices.
- `3_expectations/testing.md`: validate documentation/process-only changes by
  direct inspection.
- `3_expectations/security.md`: no security-sensitive behavior should be
  introduced.

## Proposed Approach

1. Define a canonical work filename format for both proposal and completion
   files: `YYYYMMDD-NNN-short-kebab-title.md`.
2. Add explicit naming guidance to repository workflow docs and work templates
   so future files follow the rule.
3. Rename existing files in `work/1_proposed/` and `work/2_completed/` to the
   new format using sequence numbers per date.
4. Update cross-file links and references so proposal/completion traceability
   remains valid after renames.
5. Validate with repository-wide markdown linting and targeted link inspection.

## Risks

- Renames can break intra-repo links if all references are not updated.
- Sequence assignment for historical files may be ambiguous when multiple files
  share the same date.

## Questions

- Resolved: sequence numbers are globally incremented across both work
  directories for each date.
- Resolved: ordering is based on historical git history.

## Approval Gate

Approved and implemented.
