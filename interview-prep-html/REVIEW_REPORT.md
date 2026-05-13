# Review Report - DE Interview Handbook

## Issues found

- Static Vietnamese UI text was mojibaked, including broken question/interview labels, arrows and action labels.
- Embedded answer text was readable but mostly unaccented, reducing scanability for Vietnamese learners.
- Module navigation jumped abruptly and did not maintain a reliable active state.
- Expand/collapse used hard `display` toggles, causing rough transitions and unnecessary layout jumps.
- Search ran on every keystroke without debounce.
- Large tables and code blocks needed stronger mobile overflow handling.
- Question cards lacked reading-time cues and per-module progress context.

## Fixes applied

- Preserved `<meta charset="UTF-8">` and rewrote static UI/JS text with valid UTF-8 Vietnamese.
- Normalized the embedded Vietnamese learning content with a conservative accent pass while preserving all 100 questions and existing answer structure.
- Added smooth module/question expand-collapse using `max-height` transitions.
- Added debounced search for smoother filtering.
- Added `IntersectionObserver`-based sidebar active highlighting and sidebar auto-scroll to the active module.
- Added sticky quick navigation area with progress, visible-question count, mock interview controls and validation status.
- Added per-module progress counters and per-question estimated reading time.
- Improved visual hierarchy for production examples, trade-offs, anti-patterns, cost and monitoring notes.
- Added responsive table wrappers and touch-friendly mobile behavior.

## Remaining recommendations

- The automatic accent normalization improves readability, but a native Vietnamese technical editor should review the full 100-answer corpus for wording nuance.
- For future scale, move the embedded question data into a generated JSON asset only if multi-file output becomes allowed.
- Add browser-based visual regression checks if this handbook becomes part of a larger release pipeline.
