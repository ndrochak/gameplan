# Testing Expectations

## Required

- Documentation-only changes must be validated by direct inspection of the
  affected artifacts.
- API contract changes between React and Django require contract or integration
  coverage.
- Schema changes require migration review and validation.

## Coverage Expectations

- Cover critical scheduling and participation paths where conflicts,
  double-bookings, capacity limits, or convention time boundaries are enforced.
- When executable code changes, run both test suites and confirm coverage does
  not drop below current baselines: **94% overall** for the backend
  (`DJANGO_DEBUG=true .venv/bin/python -m coverage run manage.py test
  conventions && .venv/bin/python -m coverage report --include="conventions/*,gameplan/*"`),
  **89% statements / 80% branches** for the frontend
  (`npm run test:run -- --coverage`). New code paths must be exercised by at
  least one test; untested branches must be justified in the work item.

## Regression Protection

- Bug fixes should include focused regression coverage when executable code is
  involved and the failure mode can be reproduced.

## Validation

- Validate completed work against applicable `3_expectations/` categories before
  closing the work item.

## Non-Functional Testing

- Performance-sensitive changes should include query-plan review, load testing,
  or another proportionate validation method when latency risk is material.
