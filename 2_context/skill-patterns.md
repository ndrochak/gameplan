# Skill Patterns

## Repository-Local Codex Skills

Codex skills that should travel with this repository live under:

```text
.codex/skills/<skill-name>/
```

Each skill should include:

- `SKILL.md` with `name` and `description` frontmatter.
- `agents/openai.yaml` when user-facing skill metadata is useful.

Use lowercase hyphenated skill names. Keep skill bodies concise and procedural,
and add resource directories only when the skill actually needs scripts,
references, or assets.
