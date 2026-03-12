---
name: skill-creator
description: Create or update pi skills for Brain. Use when designing, structuring, or packaging new .pi/skills/ capabilities. Skills are SKILL.md files with optional scripts/, references/, and assets/ subdirectories. Invoke when asked to create a skill, build a new capability, or package reusable knowledge into a skill.
---

# Skill Creator

This skill guides creation of effective pi skills for this repository.

## About Pi Skills

Skills are modular packages in `.pi/skills/<name>/` that extend Brain's capabilities:
- `SKILL.md` (required) — frontmatter metadata + instructions
- `scripts/` — executable code for deterministic tasks
- `references/` — documentation loaded as needed
- `assets/` — files used in output

## Skill Anatomy

```
skill-name/
├── SKILL.md          # Required: frontmatter + instructions
├── scripts/          # Optional: bash/python scripts
├── references/       # Optional: docs loaded on demand
└── assets/           # Optional: templates, files
```

### SKILL.md Frontmatter
```yaml
---
name: skill-name
description: What it does AND when to use it (this is the trigger)
---
```

The `description` is the primary trigger — make it comprehensive with "use when" examples.

## Core Principles

1. **Context is expensive** — only add what the model doesn't already know
2. **Progressive disclosure** — metadata always loaded, body on trigger, resources on demand
3. **Concise over verbose** — prefer examples over explanations
4. **No extra docs** — no README.md, CHANGELOG.md, etc. — only SKILL.md + resources

## Creating a Skill

### Step 1: Understand the skill
- What problem does it solve?
- What would trigger it? ("When the user says X...")
- What reusable resources would help?

### Step 2: Create the directory
```bash
mkdir -p .pi/skills/<skill-name>/{scripts,references}
```

### Step 3: Write SKILL.md
- Frontmatter: name + description (include trigger phrases)
- Body: concise instructions, examples, workflow steps
- Reference scripts/references files when they exist

### Step 4: Add resources (if needed)
- Scripts: deterministic operations, repeated code
- References: schemas, API docs, domain knowledge
- Assets: templates, boilerplate files

### Step 5: Test
- Use the skill on a real task
- Refine based on what worked/didn't

## Skill Naming
- Lowercase, hyphens: `skill-name`, `cosmos-query`, `idea-handoff`
- Verb-led: `create-issue`, `post-to-bulletin`
- Keep under 64 chars

## Brainstorm-Specific Skills

Good candidates for Brain skills:
- `idea-handoff` — structure and post ideas to Cosmos bulletin
- `reading-analysis` — extract insights from articles/papers
- `cosmos-query` — query and display Cosmos DB data
- `sibling-task` — create tasks for executing agents
