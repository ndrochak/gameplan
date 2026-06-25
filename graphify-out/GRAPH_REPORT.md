# Graph Report - .  (2026-06-24)

## Corpus Check
- Corpus is ~16,090 words - fits in a single context window. You may not need a graph.

## Summary
- 245 nodes · 318 edges · 35 communities (21 shown, 14 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Django Convention Models|Django Convention Models]]
- [[_COMMUNITY_Frontend React Dependencies|Frontend React Dependencies]]
- [[_COMMUNITY_Work Proposals|Work Proposals]]
- [[_COMMUNITY_Conventions API Layer|Conventions API Layer]]
- [[_COMMUNITY_Frontend TypeScript Config|Frontend TypeScript Config]]
- [[_COMMUNITY_React App Components|React App Components]]
- [[_COMMUNITY_ICE Agent Methodology|ICE Agent Methodology]]
- [[_COMMUNITY_Convention Domain Model|Convention Domain Model]]
- [[_COMMUNITY_Frontend Node Config|Frontend Node Config]]
- [[_COMMUNITY_Timezone Feature Work|Timezone Feature Work]]
- [[_COMMUNITY_System Architecture|System Architecture]]
- [[_COMMUNITY_Frontend Build Scripts|Frontend Build Scripts]]
- [[_COMMUNITY_Work Lifecycle Conventions|Work Lifecycle Conventions]]
- [[_COMMUNITY_API Hardening|API Hardening]]
- [[_COMMUNITY_Django App Config|Django App Config]]
- [[_COMMUNITY_Unknowns Resolution Skill|Unknowns Resolution Skill]]
- [[_COMMUNITY_Patterns Template Scope|Patterns Template Scope]]
- [[_COMMUNITY_Expectation Boundaries|Expectation Boundaries]]
- [[_COMMUNITY_ASGI Config|ASGI Config]]
- [[_COMMUNITY_Django Settings|Django Settings]]
- [[_COMMUNITY_WSGI Config|WSGI Config]]
- [[_COMMUNITY_Database Migrations|Database Migrations]]
- [[_COMMUNITY_Context Templates|Context Templates]]
- [[_COMMUNITY_Architecture Decision Records|Architecture Decision Records]]
- [[_COMMUNITY_Engineering Expectations Template|Engineering Expectations Template]]
- [[_COMMUNITY_Security Expectations Template|Security Expectations Template]]
- [[_COMMUNITY_Testing Expectations Template|Testing Expectations Template]]
- [[_COMMUNITY_UX Expectations Template|UX Expectations Template]]

## God Nodes (most connected - your core abstractions)
1. `Convention` - 17 edges
2. `compilerOptions` - 17 edges
3. `ConventionApiTests` - 13 edges
4. `compilerOptions` - 12 edges
5. `convention_collection()` - 10 edges
6. `convention_detail()` - 10 edges
7. `valid_convention_attrs()` - 10 edges
8. `Domain Context` - 10 edges
9. `ConventionWriteForm` - 8 edges
10. `ConventionModelTests` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Human Approval Gate (mandatory pre-implementation)` --semantically_similar_to--> `Work Item Lifecycle (proposed -> completed)`  [INFERRED] [semantically similar]
  2_context/idsd_methodology.md → AGENTS.md
- `Domain Context` --semantically_similar_to--> `Product Intent`  [INFERRED] [semantically similar]
  2_context/domain.md → 1_intent/product.md
- `Clarify Unknowns Skill` --references--> `Feature Intent: Convention Creation`  [INFERRED]
  .codex/skills/clarify-unknowns/SKILL.md → 1_intent/features/001-convention-creation.md
- `Skill Patterns` --references--> `Clarify Unknowns Skill`  [INFERRED]
  2_context/skill-patterns.md → .codex/skills/clarify-unknowns/SKILL.md
- `Product Intent` --references--> `Attendee (Actor)`  [INFERRED]
  1_intent/product.md → 2_context/domain.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **ICE Triad: Intent, Context, Expectations govern agent work** — intent_product, context_idsd_methodology, expectations_engineering_template [EXTRACTED 0.95]
- **Three-Tier Web Architecture: React → Django → PostgreSQL** — concept_react_client, concept_django_application, concept_postgresql [EXTRACTED 1.00]
- **Domain Actors: Organizer, Host, and Attendee coordinate around conventions** — concept_organizer, concept_host, concept_attendee [EXTRACTED 1.00]
- **ICE Methodology enforced by Expectations, Context, and Intent priority hierarchy** — concept_ice_methodology, 3_expectations_engineering, 3_expectations_convention, 3_expectations_testing, 3_expectations_ux, 3_expectations_product, 3_expectations_security [EXTRACTED 1.00]
- **Convention Creation proposal gates against all expectation categories** — 1_proposed_20260610_011, 3_expectations_convention, 3_expectations_engineering, 3_expectations_testing, 3_expectations_security, 3_expectations_ux, 3_expectations_product [EXTRACTED 1.00]
- **Human approval gate enforced across AGENTS.md, ICE methodology, and proposal lifecycle** — gameplan_agents, concept_human_approval_gate, concept_work_lifecycle, 1_proposed_20260610_008 [EXTRACTED 1.00]
- **Timezone Selection Feature Evolution (expectation → implementation → simplification)** — 2_completed_20260611_018_timezone_selection_expectation, 2_completed_20260611_020_timezone_selection_implementation, 2_completed_20260616_022_simplify_timezone_list [EXTRACTED 0.95]
- **ICE Workflow Governance (proposal traceability + approval gate + sortable naming)** — concept_human_approval_gate, concept_proposal_completion_traceability, concept_sortable_work_filename_convention [INFERRED 0.85]
- **API Hardening Changes (ModelForm + JSON parsing + pagination + secret key)** — 1_proposed_20260610_012_api_hardening_and_idiomatic_cleanup, 2_completed_20260610_013_api_hardening_and_idiomatic_cleanup, concept_django_modelform_validation [EXTRACTED 0.95]

## Communities (35 total, 14 thin omitted)

### Community 0 - "Django Convention Models"
Cohesion: 0.13
Nodes (9): ConventionAdmin, Meta, Convention, Meta, ConventionApiTests, ConventionModelTests, valid_convention_attrs(), valid_convention_payload() (+1 more)

### Community 1 - "Frontend React Dependencies"
Cohesion: 0.08
Nodes (25): dependencies, react, react-dom, devDependencies, eslint, @eslint/js, eslint-plugin-react-hooks, eslint-plugin-react-refresh (+17 more)

### Community 2 - "Work Proposals"
Cohesion: 0.13
Nodes (23): Work Proposal: Unknowns Resolution Skill, Work Proposal: Proposal Completion Status, Work Proposal: Patterns Template Scope Guidance, Work Proposal: Expectation Boundary Cleanup, Work Proposal: Human Approval Gate Rule, Work Proposal: Convention Creation Feature, Convention Expectations, Engineering Expectations (+15 more)

### Community 3 - "Conventions API Layer"
Cohesion: 0.23
Nodes (16): Any, Convention, convention_collection(), convention_detail(), error_response(), form_errors_to_dict(), parse_json_body(), save_form() (+8 more)

### Community 4 - "Frontend TypeScript Config"
Cohesion: 0.11
Nodes (18): compilerOptions, allowJs, allowSyntheticDefaultImports, esModuleInterop, forceConsistentCasingInFileNames, isolatedModules, jsx, lib (+10 more)

### Community 5 - "React App Components"
Cohesion: 0.12
Nodes (9): buildPayload(), Convention, ConventionFormState, emptyForm, fallbackTimezoneOptions, FieldErrors, normalizeTime(), FetchJson (+1 more)

### Community 6 - "ICE Agent Methodology"
Cohesion: 0.20
Nodes (14): Proposed Work Template, Completed: Human Approval Gate Rule, Clarify Unknowns OpenAI Agent Interface, Clarify Unknowns Skill, Agent Decision Hierarchy (Expectations > Context > Intent), Codex Skill Structure (.codex/skills/<name>/), Human Approval Gate (mandatory pre-implementation), Intent-Context-Expectations (ICE) Methodology (+6 more)

### Community 7 - "Convention Domain Model"
Cohesion: 0.24
Nodes (14): Attendee (Actor), Tabletop Convention Planning and Participation Coordination, Convention (Domain Concept), Convention Window, Host (Actor), Hosted Game, Organizer (Actor), Participation Commitment (+6 more)

### Community 8 - "Frontend Node Config"
Cohesion: 0.14
Nodes (13): compilerOptions, allowImportingTsExtensions, isolatedModules, lib, module, moduleDetection, moduleResolution, noEmit (+5 more)

### Community 9 - "Timezone Feature Work"
Cohesion: 0.31
Nodes (11): Proposed: Timezone Selection Expectation, Proposed: Timezone Selection Implementation, Proposed: Simplify Timezone List to Curated City-per-Offset Set, Completed: Convention Creation, Completed: Timezone Selection Expectation, Completed: Timezone Selection Implementation, Completed: Simplify Timezone List to Curated City-per-Offset Set, Convention Creation Feature (Django + React end-to-end) (+3 more)

### Community 10 - "System Architecture"
Cohesion: 0.36
Nodes (9): Background Processing (Django-managed), Django Application, PostgreSQL Database, React Web Client, Server-Authoritative Validation Pattern, TIMEZONE_OPTIONS Curated IANA City List, Architecture Context, Architecture Context Template (+1 more)

### Community 11 - "Frontend Build Scripts"
Cohesion: 0.29
Nodes (7): scripts, build, dev, lint, preview, test, test:run

### Community 12 - "Work Lifecycle Conventions"
Cohesion: 0.33
Nodes (6): Proposed: Work File Naming Order Convention, Completed: Proposal Completion Status, Completed: Work File Naming Order Convention, Completion Report Template, Proposal-to-Completion Traceability (Status:completed + link), Sortable Work Filename Convention (YYYYMMDD-NNN-kebab-title)

### Community 13 - "API Hardening"
Cohesion: 0.67
Nodes (3): Proposed: API Hardening and Idiomatic Cleanup, Completed: API Hardening and Idiomatic Cleanup, Django ModelForm Server-Authoritative Validation

## Knowledge Gaps
- **98 isolated node(s):** `Migration`, `Meta`, `name`, `private`, `version` (+93 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Engineering Expectations` connect `Work Proposals` to `System Architecture`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `Human Approval Gate (mandatory pre-implementation)` connect `ICE Agent Methodology` to `Timezone Feature Work`, `Work Proposals`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `Convention` connect `Django Convention Models` to `Conventions API Layer`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Convention` (e.g. with `ConventionAdmin` and `ConventionWriteForm`) actually correct?**
  _`Convention` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Migration`, `Meta`, `ASGI config for the Gameplan project.` to the rest of the system?**
  _105 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Django Convention Models` be split into smaller, more focused modules?**
  _Cohesion score 0.12643678160919541 - nodes in this community are weakly interconnected._
- **Should `Frontend React Dependencies` be split into smaller, more focused modules?**
  _Cohesion score 0.07692307692307693 - nodes in this community are weakly interconnected._