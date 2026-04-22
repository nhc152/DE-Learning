# task-template.md

## Reusable Task Template for Claude

Use this template when assigning a new tutorial generation task.

---

Use project rules from `.claude`.

Current task:
Create `[TARGET_FILE_NAME]`

Allowed sources only:
- `./data-engineer-handbook/`
- `./DE_Roadmap_Expert_NHC.md`
- `./PROMPT_Build_DE_Tutorial_HTML.md`
- `./Week00_Setup.html`

Do not read any other files.

Requirements:
- follow the structure and interaction style of `Week00_Setup.html`
- follow the tutorial build rules from `PROMPT_Build_DE_Tutorial_HTML.md`
- align content with `DE_Roadmap_Expert_NHC.md`
- use Vietnamese explanations
- include PostgreSQL and Oracle SQL where relevant
- keep the tutorial polished, standalone, and self-study friendly
- keep review questions at exactly 10 for each relevant module if requested

If information is missing, stop and tell me what is missing instead of reading more files.

---

## Example 1
Use project rules from `.claude`.

Current task:
Create `Week02_Python_DE.html`

Allowed sources only:
- `./data-engineer-handbook/`
- `./DE_Roadmap_Expert_NHC.md`
- `./PROMPT_Build_DE_Tutorial_HTML.md`
- `./Week00_Setup.html`

Do not read any other files.

Requirements:
- follow the structure and interaction style of `Week00_Setup.html`
- align content with week 2 Python for DE from roadmap
- use Vietnamese explanations
- include PostgreSQL and Oracle SQL where relevant
- 10 review questions for each module

---

## Example 2
Use project rules from `.claude`.

Current task:
Revise `Week02_Python_DE.html`

Allowed sources only:
- `./data-engineer-handbook/`
- `./DE_Roadmap_Expert_NHC.md`
- `./PROMPT_Build_DE_Tutorial_HTML.md`
- `./Week00_Setup.html`

Do not read any other files.

Requirements:
- improve visual consistency
- preserve structure
- preserve Vietnamese output
- expand practice tasks
- keep all JS interactions working