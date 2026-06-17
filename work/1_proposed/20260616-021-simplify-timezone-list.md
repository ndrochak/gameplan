# Proposed Work

## Metadata

- Work Item: Simplify Timezone List to Curated City-per-Offset Set
- Owner: Product
- Date: 2026-06-16
- Status: completed
- Approval Evidence: User instructed implementation directly in conversation on
  2026-06-16 ("i don't like the time zone list. it's too long. Let's use a
  simpler version that offers just one major city per time zone, like Tokyo for
  +9"). Retroactive artifact — implementation preceded this proposal due to
  agent error (ponytail mode overrode ICE gate).
- Completion Report:
  `work/2_completed/20260616-022-simplify-timezone-list.md`

## Intent Reference

- `1_intent/features/001-convention-creation.md`

## Intent Delta (Optional)

Reduce the timezone selection list from the full `zoneinfo.available_timezones()`
set (500+ entries) to a curated list of one representative major city per UTC
offset, including UTC itself. This is a UX scope reduction: the expectation that
timezone selection uses standard IANA identifiers and a selectable UI is
unchanged; only the population of the list changes.

## Relevant Context

- `2_context/architecture.md`: timezone options are served by Django; the client
  uses whatever the endpoint returns. Changing the endpoint population requires
  no client-side changes beyond the dropdown contents updating.
- `2_context/domain.md`: timezone values must be valid IANA identifiers.
  All entries in a curated list must still pass `ZoneInfo` validation.
- `work/2_completed/20260611-020-timezone-selection-implementation.md`:
  identified "consider a searchable combobox if the native select becomes
  cumbersome with the full runtime IANA timezone list" as a follow-up risk.
  This work addresses the root cause by reducing list length instead.

## Expectations

- `3_expectations/convention.md`: timezone selection must use standard IANA
  timezone identifiers through a selectable UI — met by any valid curated list.
- `3_expectations/engineering.md`: changes must not break existing API
  contracts. The endpoint shape (`{"timezones": [...]}`) is unchanged; only
  the contents narrow.
- `3_expectations/testing.md`: behavioral changes to the endpoint require
  updated test coverage.
- `3_expectations/ux.md`: the selectable control must remain accessible and
  keyboard-operable — unchanged by this work.

## Proposed Approach

1. Replace `available_timezones()` in `backend/conventions/api.py` with a
   hardcoded `TIMEZONE_OPTIONS` list: one representative IANA city per UTC
   offset from UTC-11 through UTC+12, plus UTC itself.
2. Remove the now-unused `from zoneinfo import available_timezones` import.
3. Update `backend/conventions/tests.py` to reflect the curated list behavior:
   remove the sorted-order assertion (list is ordered by offset, not
   alphabetically), remove the UTC assertion (it is now explicit), add an
   upper-bound length check.
4. Update `2_context/architecture.md` to replace the stale `available_timezones()`
   reference with the curated list description.

## Risks

- Organizers in UTC offsets not represented by a well-known city may find no
  familiar entry. Mitigated by including UTC and covering all major populated
  offsets including half-hour and quarter-hour offsets (India, Iran, Nepal,
  Myanmar).
- Existing conventions persisted with a timezone value not in the curated list
  (e.g., `America/Chicago`) remain valid at the model layer since `ZoneInfo`
  validation is offset-agnostic; the frontend already handles this case by
  prepending the saved value if it is absent from the option list.

## Questions

- None.

## Approval Gate

Retroactive artifact. Implementation was approved implicitly by the user's
direct instruction in conversation on 2026-06-16. Agent error: ICE gate was
not respected before implementation began.
