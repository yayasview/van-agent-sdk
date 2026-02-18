# Contributing — How to Create New Skills

## Skill Structure

Every skill lives in `skills/<skill-name>/` and must contain:

```
skills/<skill-name>/
├── SKILL.md        # Skill definition (required)
└── examples/       # Example outputs (recommended)
```

## SKILL.md Format

```markdown
---
name: skill-name
description: >
  One-line description of what this skill does.
  Trigger phrases: "natural language triggers that invoke this skill"
---

# Skill Name

## Dependencies
- List any required MCP connections or other skills

## Inputs
- What the skill needs to run (mark required vs optional)

## Workflow
1. Step-by-step process the skill follows
2. Be specific enough that the agent can execute without ambiguity

## Output Format
Exact template of what the skill produces

## Quality Checks
- Validation criteria for the output
- Edge cases to handle

## Examples
Reference the examples/ folder
```

## Registering a Skill

After creating the skill:

1. Add it to `skill-registry.md` in the Active Skills table
2. If the skill needs a slash command, create `commands/<skill-name>.md`

## Slash Command Format

Commands are thin wrappers:

```markdown
[One sentence describing what this command does]. Read and execute the skill at `skills/<skill-name>/SKILL.md`.

Usage: /<command-name> [arguments]

[Any context about where to find input data or how to handle edge cases.]
```

## Guidelines

- Skills should be standalone when possible (no dependencies on other skills)
- Always include quality checks — the agent should self-validate output
- Include real examples in the `examples/` folder once available
- Keep SKILL.md focused on the workflow, not background context (that goes in knowledge files)
- Test with at least 5 real inputs before marking a skill as "Active" in the registry
