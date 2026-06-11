# Domain Context

## Domain Overview

The product domain is tabletop convention planning and participation
coordination. It helps organizers define conventions, helps hosts plan and fill
hosted games, and helps attendees commit to games ahead of the event so
convention time is spent playing rather than searching.

## Core Concepts

- Convention: The event container that defines scheduling boundaries and
  attendance limits.
- Convention Window: Start date, end date, timezone, and daily open-hours rules
  that determine when game scheduling applies.
- Hosted Game: A game offered by a host for attendee participation.
- Participation Commitment: An attendee commitment to join a hosted game,
  used by hosts for planning and material preparation.
- Capacity: Event-level attendance limit used to constrain participation at the
  convention level.
- Schedule Integrity: Conflict and double-booking prevention goals for
  conventions and participants.

## Actors

- Organizer: Creates and edits conventions; defines event-level timing, location,
  and attendance capacity. Can also participate in games as an attendee.
- Host: Offers games and relies on participant commitments to prepare copies,
  rules summaries, and materials. Can also participate in games as an attendee.
- Attendee: Commits to games within a convention schedule and uses convention
  details to understand where and when participation applies. This role is not
  exclusive and may be held by organizers and hosts.

## Key Workflows

- Convention creation and editing: Organizer defines start date, end date,
  free-text location, organizer-provided timezone, one continuous daily
  open-hours window, and maximum attendance capacity.
- Convention-aligned planning: Hosts and attendees use convention boundaries to
  coordinate game participation.
- Pre-convention commitment: Participants commit before the convention so hosts
  can plan reliably and reduce no-shows.

## Terminology

- Convention: A specific event instance where scheduling and participation occur.
- Host: A user who offers a game session.
- Attendee: A participation role for users joining convention activities and
  game sessions; organizers and hosts may also act in this role.
- Organizer-provided timezone: Timezone selected by the organizer as the
  convention's scheduling reference.
- Daily open-hours window: A single continuous time range per day during which
  convention scheduling is valid.
- Double-booking: A conflicting commitment where a participant or slot overlaps
  another scheduled commitment.

## Domain Constraints

- The product is not a social network for gamers.
- The product is not a full registration or ticketing system.
- Initial convention modeling does not include multiple venues or complex
  room-level scheduling.
- Convention search and discovery are out of scope.
- Convention definition currently requires one continuous daily open-hours
  window, not multiple windows.
- Convention boundaries and capacity are organizer-defined and serve as source
  constraints for downstream scheduling behavior.
- Convention timezone values must be valid IANA timezone identifiers.
