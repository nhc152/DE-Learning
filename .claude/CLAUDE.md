# CLAUDE.md

## Project
DE-LEARNING

## Project Goal
Build standalone weekly HTML tutorials for Data Engineering learners, based on:
- data-engineer-handbook
- DE_Roadmap_Expert_NHC.md
- PROMPT_Build_DE_Tutorial_HTML.md
- Week00_Setup.html

The tutorials must be polished, interactive, beginner-friendly, and consistent across all weeks.

---

## Allowed Sources Only
Claude may read ONLY these sources unless the user explicitly approves more:

1. `./data-engineer-handbook/`
2. `./DE_Roadmap_Expert_NHC.md`
3. `./PROMPT_Build_DE_Tutorial_HTML.md`
4. `./Week00_Setup.html`

---

## Forbidden Actions
Do NOT:
- read any other file outside the allowlist
- scan parent folders
- inspect sibling folders
- use globbing to include unrelated files
- infer content from non-allowed local files
- modify the source reference files
- silently read generated week files unless the user explicitly asks

If required information is missing, stop and report the gap instead of reading more files.

---

## Output Language Policy
All generated tutorial content must be written in Vietnamese.

Use:
- natural Vietnamese
- practical mentor-style explanations
- beginner-friendly wording
- professional but easy-to-understand phrasing

Keep technical keywords in English when they are standard, for example:
- PostgreSQL
- Oracle SQL
- Docker
- Python
- Airflow
- dbt
- Spark
- Kafka
- Window Function
- API
- ETL / ELT

UI labels in generated HTML should remain in Vietnamese.

---

## Output Rules
Default output target:
- create or update only `WeekXX_*.html`

Do not create extra files unless the user asks.

Generated HTML must:
- follow the structure and interaction style of `Week00_Setup.html`
- align with rules from `PROMPT_Build_DE_Tutorial_HTML.md`
- align topic scope with `DE_Roadmap_Expert_NHC.md`
- remain standalone HTML with embedded CSS/JS unless user asks otherwise
- be suitable for self-study without backend

---

## Structure Rules
Each module must preserve the required section order:

1. Menu Tổng Thể
2. Mục Đích Module
3. Giải Thích Chi Tiết
4. Câu Hỏi Ôn Tập
5. Tổng Kết
6. Bài Tập Thực Hành

Preserve the overall layout pattern:
- Hero
- Badge row
- Sidebar navigation
- Main content modules
- Collapsible sections
- Interactive quiz
- Practice solution toggle
- Final mini test when appropriate

Preserve core interaction functions where applicable:
- `showModule`
- `goNext`
- `goPrev`
- `toggleSection`
- `answerQuiz`
- `toggleSolution`
- `gradeFinalTest`
- `resetFinalTest`

---

## SQL Policy
Where relevant, include both:
- PostgreSQL
- Oracle SQL

When syntax differs:
- present both versions clearly
- explain the difference briefly in Vietnamese
- do not force Oracle examples where the topic is purely Python-only, but do include SQL usage where relevant to DE workflows

---

## Quiz Policy
When the user requests review questions for each part/module:
- provide exactly 10 questions for each relevant module
- keep them practical
- include explanation feedback for answers when using interactive quiz format

---

## Quality Standard
Generated content should be:
- practical
- visually consistent
- logically structured
- not overly academic
- rich in examples
- suitable for learners moving from ETL + SQL into Data Engineering

Prefer:
- real-world pipeline examples
- production mindset
- operational reasoning
- naming clarity
- explicit trade-offs

---

## Behavior Before Starting a New Week
Before generating a new tutorial:
1. Restate the allowed sources internally
2. Use only the allowed sources
3. Identify the target week/topic from roadmap
4. Reuse the HTML structure from `Week00_Setup.html`
5. Apply the build rules from `PROMPT_Build_DE_Tutorial_HTML.md`
6. Generate the target `WeekXX_*.html`

If ambiguity exists, ask a focused question instead of assuming.

---

## Editing Existing Week Files
If the user asks to revise an existing `WeekXX_*.html`:
- preserve the existing style unless asked to redesign
- keep the same language policy
- avoid breaking JS interactions
- do not degrade formatting consistency

---

## Default Working Mode
Assume this project is a long-term tutorial system.
Optimize for:
- consistency across weeks
- reusable structure
- clean educational UX
- clear Vietnamese teaching style