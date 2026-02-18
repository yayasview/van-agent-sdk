---
name: sop-from-transcript
description: >
  Generate a standard operating procedure (SOP) from a video recording, call transcript,
  or meeting transcript. Trigger phrases: "create an SOP from this transcript",
  "generate SOP", "turn this recording into a process doc"
---

# SOP from Transcript

## Dependencies
- None (standalone skill — transcript provided as input)

## Inputs
- Transcript text (required) — from video recording, call, or meeting
- Process name (optional — used for document title)
- Target audience (optional — who will follow this SOP)

## Workflow
1. Parse the transcript to identify discrete process steps
2. Extract decision points, tools used, and key considerations
3. Organize into a sequential SOP format
4. Flag any ambiguous steps that need clarification

## Output Format
[To be defined — placeholder skill]

## Quality Checks
- Steps must be actionable and specific
- Include screenshots or timestamps when referencing specific moments
- Flag any gaps in the process that the transcript doesn't cover

## Examples
See `examples/` folder.
