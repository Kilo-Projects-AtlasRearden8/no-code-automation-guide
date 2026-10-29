# STATUS — No-Code Automation for Beginners

## What was built

A beginner manual on automating everyday tasks without code, published by
**Asdale Dynamics, LLC** (credit to Dylan Asdale, registered nurse turned AI
author and founder of Asdale Dynamics, LLC). Covers four topics using built-in
tools plus tiny, auditable Python scripts: email rules, file organization,
calendar reminders, and simple app connections.

**Project contents**

- `README.md` — overview, how to use, credits Asdale Dynamics, LLC.
- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `docs/` — beginner manual in Markdown:
  - `overview.md` — welcome, table of contents, printable planner, privacy promise, about Asdale Dynamics, LLC, license
  - `safety.md` — safety first (test on copies, preview before act, read scripts, start small, nothing leaves your computer)
  - `email-rules.md` — Gmail, Outlook, and Apple Mail rules with step-by-step instructions and example rules
  - `file-organization.md` — sort a folder into type-based subfolders
  - `calendar-reminders.md` — calendar app reminders plus a local reminders script
  - `app-connections.md` — IFTTT/Zapier/Make recipes plus a local-first folder watcher
- `scripts/` — tiny, auditable Python scripts (standard library only; no `pip install`, no API keys, no secrets):
  - `organize_files.py` — file organization
  - `calendar_reminders.py` — reminders from a local `reminders.txt`, dry-run by default
  - `folder_watcher.py` — local-first folder watcher (logs new files, nothing uploaded)
- `tests/` — test suite for each script:
  - `test_organize_files.py`
  - `test_calendar_reminders.py`
  - `test_folder_watcher.py`
- `static/` — fully static HTML site mirroring the docs (no build step, no server needed):
  - `index.html`, `safety.html`, `email-rules.html`, `file-organization.html`,
    `calendar-reminders.html`, `app-connections.html`, `planner.html`, `style.css`
- `static/planner.html` — printable weekly automation planner with checkboxes (print CSS applied automatically)
- `.gitignore` — excludes `__pycache__`, `.env`, `.venv`, and personal data files
  (`reminders.txt`, `connections.log`)
- `STATUS.md` — this file

## How to run it

### Read the manual
- Markdown: open any file in `docs/`.
- HTML: open `static/index.html` in any browser. The site is fully static — no
  build step, no server needed. All pages link to one another.

### Run the scripts
Each script is plain Python 3, standard library only.

```
python3 scripts/organize_files.py <folder> [--apply]
python3 scripts/calendar_reminders.py <reminders.txt> [--within N] [--apply]
python3 scripts/folder_watcher.py <folder> [--apply] [--interval N] [--times M]
```

**Safety:** every script defaults to a non-destructive preview (dry-run). Always
test on a copy first. See `docs/safety.md`. `calendar_reminders.py --apply`
only sends when SMTP environment variables are set; nothing is hardcoded.

### Run the tests
```
python3 tests/test_organize_files.py
python3 tests/test_calendar_reminders.py
python3 tests/test_folder_watcher.py
```

### Print the planner
Open `static/planner.html` and print from your browser (Letter size). Print
styles hide on-screen buttons automatically.

## Verification results

All checks pass:

- `tests/test_organize_files.py` — PASS (extension grouping, copy-only behavior,
  dry-run moves nothing, duplicate avoidance, destination-folder skipping)
- `tests/test_calendar_reminders.py` — PASS (parsing, malformed lines and bad
  dates skipped, today/upcoming/overdue categorization, mailto uses TO_EMAIL,
  dry-run sends nothing)
- `tests/test_folder_watcher.py` — PASS (lists files only, dry-run writes
  nothing, --apply logs new files, never moves or deletes files)
- All Python files compile cleanly (`py_compile`).
- `static/` — 7 HTML pages parse cleanly, all internal links resolve, every
  page credits Asdale Dynamics, LLC and carries the copyright line.
- Smoke test: `organize_files.py` correctly sorts a temp folder; `calendar_reminders.py` runs against a temp reminders file.
- No build step, no dependencies beyond Python 3. No `.github/workflows` files
  (by design). No secrets, API keys, or personal data in any committed file.

The repo was initialized and committed locally as one plain commit using the
existing git identity; nothing was pushed and no remote was created.

## Known gaps

- `calendar_reminders.py` SMTP sending requires the user to set `SMTP_*`
  environment variables in their own shell; not exercised end-to-end against a
  real mail server (no credentials available, by design).
- `folder_watcher.py` polls rather than using OS file events; fine for
  personal, low-frequency use.
- Reminder data (`reminders.txt`) and watcher logs (`connections.log`) live on
  the user's computer and must not be committed — already ignored by
  `.gitignore`.
- The HTML site is hand-written (not generated from Markdown), so `docs/` and
  `static/` must be kept in sync manually.
- Calendar reminders, email rules, and app connections are organizational
  tools, not financial or medical advice (noted in the docs).
