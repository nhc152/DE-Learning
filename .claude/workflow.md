# workflow.md

## Standard Workflow for Creating a New Week

### Step 1 — Identify Target
Determine which week/tutorial the user wants to build.

Examples:
- Week02_Python_DE.html
- Week03_Data_Cleaning.html
- Week04_Pipeline_Thinking.html

### Step 2 — Read Only Approved Inputs
Use only:
- `DE_Roadmap_Expert_NHC.md`
- `PROMPT_Build_DE_Tutorial_HTML.md`
- `Week00_Setup.html`
- `data-engineer-handbook/`

### Step 3 — Extract the Right Signals
From roadmap:
- week scope
- learning objectives
- artifact expectations
- topic boundaries

From build prompt:
- structure rules
- required sections
- interaction components
- JS behavior

From Week00:
- visual style
- component implementation
- naming and layout patterns

From handbook:
- topic details
- practical technical substance

### Step 4 — Compose the Tutorial
Generate a standalone HTML file that:
- matches the project style
- uses Vietnamese explanations
- stays beginner-friendly
- includes practical examples
- includes PostgreSQL and Oracle SQL when relevant

### Step 5 — Validate Before Finalizing
Check:
- layout consistency
- section order correctness
- quiz presence
- summary presence
- practice section presence
- language consistency
- technical correctness
- SQL policy alignment

---

## Standard Workflow for Revising an Existing Week

### Use this when:
- user asks to improve or extend a generated week
- user wants more quiz questions
- user wants more practice tasks
- user wants a visual refresh

### Rules:
- preserve file identity
- preserve tutorial structure unless redesign requested
- do not break existing JS interactions
- do not silently change the lesson scope

---

## When to Ask Questions
Ask a short clarifying question only if:
- target week is ambiguous
- the requested topic is outside roadmap
- the user wants additional non-allowlisted references
- the requested output format conflicts with project rules

Do not ask unnecessary questions if the requested target is clear.

---

## Default Decision Rules
If the user says:
- "build next week" → infer next roadmap week
- "same format as Week00" → follow `Week00_Setup.html`
- "the questions should be 10 per part" → enforce exactly 10 review questions per relevant module
- "use Oracle and PostgreSQL" → provide both where relevant

---

## Final Output Habit
When producing a tutorial:
- keep it clean
- keep it consistent
- keep it realistic
- keep it reusable