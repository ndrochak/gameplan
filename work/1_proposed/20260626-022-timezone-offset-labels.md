# Proposed Work: Add UTC offset labels to timezone options and start list from UTC+0

## Metadata

- Work Item: Timezone option labels should include UTC offsets and begin at UTC+0
- Owner: Product
- Date: 2026-06-26
- Status: completed
- Approval Evidence: approved by user in conversation on 2026-06-26
- Completion Report:
  `work/2_completed/20260626-023-timezone-offset-labels.md`

## Intent Reference

- `1_intent/features/001-convention-creation.md`

## Intent Delta (Optional)

Update the curated convention timezone options so each option includes the UTC offset in its presentation text, and order the list beginning at UTC+0. This is a UX clarity enhancement for timezone selection.

## Relevant Context

- `2_context/architecture.md`: timezone options are served by Django from a curated list in `backend/conventions/api.py`.
- `2_context/domain.md`: convention timezone values must remain valid IANA timezone identifiers.
- `work/1_proposed/20260616-021-simplify-timezone-list.md`: the current option set is a curated city-per-offset list rather than the full IANA list.

## Expectations

- `3_expectations/convention.md`: timezone selection must use standard IANA timezone identifiers through a selectable UI.
- `3_expectations/engineering.md`: API contract changes should be compatible with the existing frontend and not break clients.
- `3_expectations/ux.md`: the selectable timezone control must remain accessible and keyboard-operable.
- `3_expectations/testing.md`: updates to timezone option behavior require regression coverage.

## Proposed Approach

1. Modify the timezone options endpoint in `backend/conventions/api.py` so the list is ordered starting at UTC+0, then progressing through positive offsets and any remaining offsets.
2. Add offset-aware presentation metadata for each item, for example by returning an array of objects with `timezone` and `label` fields, where `label` includes the offset prefix (e.g. `UTC+3 Europe/Moscow`).
3. Preserve the canonical timezone identifier as the persisted value for `Convention.timezone` and the submitted payload.
4. Update the frontend timezone selector to render the new offset-aware display labels while continuing to submit the underlying IANA timezone identifier.
5. Update backend and frontend tests to cover the new option ordering and display labels.
6. Document the change in `2_context/architecture.md` if the backend payload shape or returned list semantics are updated.

## Risks

- Changing the timezone endpoint payload shape may require coordinated frontend and backend updates.
- Some users may expect the first item to be their local timezone rather than UTC+0; this proposal intentionally orders by offset for clarity and predictability.
- A label-only UX change should preserve accessibility; any new option formatting must still work with screen readers and keyboard navigation.

## Questions

- Should the new option list remain a simple string array, or should the backend return richer objects with explicit `value` and `label` fields?
- Should UTC+0 appear once as `UTC` or twice with both `UTC` and a representative city like `Europe/London`?

## Approval Gate

Status: completed

Implementation completed on 2026-06-26.