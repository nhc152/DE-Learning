# allowed-sources.md

## Strict Allowlist

Only the following local sources are allowed for reading:

1. `./data-engineer-handbook/`
2. `./DE_Roadmap_Expert_NHC.md`
3. `./PROMPT_Build_DE_Tutorial_HTML.md`
4. `./Week00_Setup.html`

## Not Allowed
Do not read:
- any other local files
- any sibling project files
- any parent directory files
- any hidden caches not explicitly approved
- generated week files unless the user explicitly asks to compare or edit them

## If Information Is Missing
If the allowlisted files do not contain enough information:
- stop
- state what is missing
- ask the user for permission before reading anything else

## Source Priority
Use sources in this priority order:

1. `DE_Roadmap_Expert_NHC.md`
   - determines scope, week topic, learning objectives

2. `PROMPT_Build_DE_Tutorial_HTML.md`
   - determines tutorial generation rules and mandatory components

3. `Week00_Setup.html`
   - determines concrete implementation style, CSS/JS patterns, layout behavior

4. `data-engineer-handbook/`
   - determines detailed technical references and supporting content

## Reference File Safety
Never modify the allowed reference files.
They are source-of-truth inputs only.