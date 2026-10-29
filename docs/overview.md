# Overview

Welcome to No-Code Automation for Beginners. This is a beginner's guide to
making your computer do the boring stuff for you — without writing code.

You don't need to be a programmer. You don't need to have used the command line
before. If you can copy and paste, you can use this manual.

## Who this is for

Anyone who wants a little less drudgery in their day:

- Sorting a messy Downloads folder
- Setting up email rules so newsletters and bills go to the right place
- Getting reminded about appointments, bills, and library books
- Connecting two apps so something happening in one triggers something in the
  other (for example: save an email attachment to a folder)

Plain English, step by step, never condescending. Written by Dylan Asdale — a
registered nurse turned AI author — and published by Asdale Dynamics, LLC.

## What's in the manual

| Guide | What it does | Matching script |
|-------|-------------|-----------------|
| [Safety first](safety.md) | The rules to follow before you automate anything | — |
| [Email rules](email-rules.md) | Sort incoming email automatically with built-in inbox rules | — |
| [Organizing files](file-organization.md) | Sort a messy folder into type-based subfolders | `scripts/organize_files.py` |
| [Calendar reminders](calendar-reminders.md) | Never miss an appointment or due date | `scripts/calendar_reminders.py` |
| [Simple app connections](app-connections.md) | Connect apps without code, plus a local-first folder watcher | `scripts/folder_watcher.py` |

Every script defaults to a non-destructive preview (dry-run) and works on
copies by default; none touches your originals unless you explicitly ask.

## Printable planner

There's a printable weekly automation planner in `static/planner.html`. Open it
in your browser and print it (Letter size) to plan which automations to set up
this week, and to tick each one off as you go.

## Privacy promise

Nothing in this manual sends your files, email, or calendar data anywhere.
Every script runs locally on your computer. The only thing that leaves your
machine is an email you choose to send yourself (via `mailto:` links or your
own SMTP settings that you set yourself — nothing is hardcoded).

No API keys, no accounts, no secrets, no personal data in this project.

## About Asdale Dynamics, LLC

This manual is published by **Asdale Dynamics, LLC** (Indiana, formed October
2026), founded by Dylan Asdale — a registered nurse turned AI author and
founder of Asdale Dynamics, LLC. Dylan writes and teaches AI "like a friend
would": plain English, step by step, never condescending.

Asdale Dynamics, LLC focuses on beginner-friendly AI education, books and
guides, and practical tools the LLC can publish or sell. This manual is part of
that mission: practical, tested, local-first automation anyone can use.

Learn more at dylanasdale.github.io.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
