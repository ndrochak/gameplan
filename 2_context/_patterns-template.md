# Preferred Engineering Patterns Template

## Scope

Use this template for repeatable local ways of working within the existing
system reality.

Architecture context answers: "What is the system shape?"

Pattern context answers: "How do we usually do recurring work here?"

Keep architecture-level patterns in `2_context/architecture.md` when they affect
system boundaries, component ownership, persistence boundaries, integration
points, or major architectural risks.

Use pattern context files for recurring conventions such as API shape,
component organization, validation style, testing style, naming conventions,
migration habits, repository-local skill structure, and other implementation
habits that future work should reuse.

Prefer scoped pattern files such as `api-patterns.md`, `frontend-patterns.md`,
`testing-patterns.md`, or `skill-patterns.md` when the guidance is specific to
one area. Avoid creating a broad catch-all patterns file until enough recurring
conventions exist to justify it.

## API Design

- [Preferred API style]
- [Error handling pattern]

## Frontend

- [UI architecture preference]
- [Component and styling guidance]

## Data Access

- [Data access pattern]

## Testing

- [Testing strategy preference]

## Additional Patterns

- [Pattern name: when to use]
