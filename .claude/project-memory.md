# project-memory.md

## Project Identity
This project builds a full Data Engineering learning roadmap as interactive HTML tutorials.

The learner profile:
- already knows ETL and SQL at a basic level
- wants to become strong in Data Engineering
- prefers practical and structured learning
- benefits from mentor-style explanation in Vietnamese

---

## Teaching Style
Preferred teaching style:
- mentor-like
- direct
- practical
- step-by-step
- not verbose for no reason
- explain "why" before "how" when useful
- prioritize clarity over jargon

Avoid:
- vague advice
- overly abstract theory without examples
- mixed language output unless needed for technical terms
- dry textbook tone

---

## Output Language Memory
Generated content should be:
- Vietnamese for explanations
- English for code syntax and SQL keywords
- Vietnamese for section labels, buttons, quiz text, summaries, practice instructions

Examples:
- good: "Mục tiêu module", "Câu hỏi ôn tập", "Bài tập thực hành"
- good: `SELECT`, `JOIN`, `GROUP BY`, `create_engine(...)`
- good: explain SQL differences in Vietnamese

---

## HTML Experience Memory
The HTML tutorials should feel:
- modern
- dark themed
- clean
- focused
- interactive
- self-study friendly

The user likes:
- sidebar navigation
- collapsible sections
- code blocks with terminal-style headers
- practical exercises
- quizzes with immediate feedback
- structured summaries
- final mini tests

---

## Content Preferences
Prioritize:
- practical Data Engineering workflows
- realistic examples
- data pipeline thinking
- debugging mindset
- operational awareness
- schema and data quality awareness
- production-oriented habits

Do not over-focus on:
- pure academic definitions
- excessive history/background
- too many unrelated side topics

---

## SQL Memory
Where suitable, show:
- PostgreSQL version
- Oracle SQL version

Typical handling:
- if syntax is same, mention both briefly
- if syntax differs, show separate code blocks
- explain differences clearly and briefly

Use SQL in realistic DE contexts such as:
- validation
- load checks
- incremental logic
- profiling
- deduplication
- extraction queries

---

## Python for DE Memory
When generating Python-focused lessons:
- emphasize ETL thinking
- organize code into extract / transform / load
- prefer maintainable structure over clever code
- include logging, error handling, validation, modularization when relevant
- connect Python lessons to databases and pipelines

---

## Quality Memory
A good generated week should:
- feel like part of the same series as Week00
- have clear module progression
- be usable as a standalone study file
- be polished enough to keep for long-term project use

A weak output is one that:
- drifts from the Week00 style
- becomes too generic
- lacks practical examples
- ignores PostgreSQL / Oracle SQL policy where relevant
- mixes English/Vietnamese inconsistently

---

## Continuity Memory
This project is intended to grow week by week.

Always optimize for:
- consistency with prior weeks
- maintainability
- easy extension into future weeks
- reusable tutorial architecture