# Architecture Context

## System Overview

The product uses a three-tier web architecture:

- React provides the client application and user interaction flows.
- Django provides the server-side application, domain logic, and APIs.
- PostgreSQL provides durable relational storage for conventions, schedules,
  participation, and related entities.

The frontend communicates with Django over HTTPS APIs. Django is the only layer
that reads and writes PostgreSQL.

## Major Components

- React Web Client: Renders organizer, host, and attendee workflows and calls
  backend APIs.
- Django Application: Owns business logic, validation, authorization, and API
  endpoints.
- PostgreSQL Database: Stores normalized domain entities and transactional
  records.
- Background Processing (Django-managed): Handles asynchronous jobs such as
  notifications, reminders, and data maintenance tasks.

## Boundaries

- React boundary:
  UI state, client-side validation for responsiveness, and API interaction only.
  No business-critical rules are enforced exclusively in the browser.
- Django boundary:
  Source of truth for domain rules, policy checks, and orchestration of write
  operations.
- PostgreSQL boundary:
  Persistence, indexing, constraints, and transactional integrity.
- Cross-component boundary:
  All data access from clients flows through Django APIs; clients do not connect
  directly to PostgreSQL.

## Integration Points

- Browser to React application delivery (static assets and runtime requests).
- React to Django API integration over HTTPS (JSON payloads).
- Django to PostgreSQL connection using ORM-managed models and migrations.
- Optional external integrations via Django adapters (email delivery,
  authentication providers, analytics).

## Existing Patterns

- Prefer server-authoritative validation in Django, with client validation as a
  user-experience enhancement.
- Keep domain modeling relational-first in PostgreSQL with explicit constraints
  (unique keys, foreign keys, and check constraints where appropriate).
- Use API versioning and backward-compatible contract evolution to reduce client
  breakage.
- Keep frontend components focused on presentation and interaction; centralize
  business policy in Django services/modules.
- Apply migrations for all schema evolution; avoid manual database drift.

## Architecture Risks

- API contract drift between React and Django can cause runtime regressions.
  Mitigation: version endpoints and add contract/integration tests.
- Long-running synchronous Django requests may degrade responsiveness.
  Mitigation: move expensive work to background processing.
- Poor indexing strategy in PostgreSQL can create latency under growth.
  Mitigation: monitor query plans and add targeted indexes.
- Coupling UI flows tightly to backend response shape can reduce iteration
  speed.
  Mitigation: use stable API response contracts and compatibility shims.
