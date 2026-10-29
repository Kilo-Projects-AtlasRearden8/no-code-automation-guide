# No-Code Automation for Beginners

Automate everyday tasks without writing code: email rules, file organization,
calendar reminders, and simple app connections — using tools you already have,
plus tiny, auditable scripts you can read end to end. Test on copies, never
move originals. Everything stays on your computer unless you choose otherwise.

You don't need to be a programmer. You don't need to have used the command
line before. If you can copy and paste, you can use this manual. Plain
English, step by step, never condescending.

**Credit:** This manual is published by **Asdale Dynamics, LLC** (Indiana,
formed October 2026), founded by Dylan Asdale — a registered nurse turned AI
author and founder of Asdale Dynamics, LLC. Dylan writes and teaches "like a
friend would": plain English, step by step, never condescending. Learn more at
dylanasdale.github.io.

---

## Who this is for

Anyone who wants a little less drudgery in their day:

- Sorting a messy Downloads folder
- Setting up email rules so newsletters and bills go to the right place
- Getting reminded about appointments, bills, and library books
- Connecting two apps so something happening in one triggers something in the other

You don't need to buy anything, create any accounts, or share any personal
data. Everything in this manual runs locally on your own computer.

## What you need

- A computer (Windows, Mac, or Linux)
- Python 3 (already on most Macs and Linux PCs; download it free from python.org if you need it)
- About ten minutes to read the safety page first

That's it. No paid accounts, no API keys, no subscriptions.

---

## What's inside

| Topic | What it does | Where |
|-------|-------------|-------|
| Safety first | The rules to follow before you automate anything | `docs/safety.md` |
| Email rules | Sort incoming email automatically (Gmail, Outlook, Apple Mail) | `docs/email-rules.md` |
| Organizing files | Sort a messy folder into type-based subfolders | `docs/file-organization.md` + `scripts/organize_files.py` |
| Calendar reminders | Never miss an appointment, bill, or due date | `docs/calendar-reminders.md` + `scripts/calendar_reminders.py` |
| App connections | Connect apps without code, plus a local-first folder watcher | `docs/app-connections.md` + `scripts/folder_watcher.py` |
| Printable planner | A weekly planner to plan and track your automations | `static/planner.html` |

## How to use this manual

1. **Read the safety page first** (`docs/safety.md`). The golden rule: test on
   copies, never move originals.
2. Pick a topic and read its guide in `docs/`. Each one is step by step.
3. Where a script is involved, run it on a test copy of your files first, then
   decide whether to use it on your real files.
4. Print `static/planner.html` and use it to plan which automations to set up
   this week.

You can read the Markdown files in `docs/` directly, or open the fully static
HTML site at `static/index.html` in any browser — no build step, no server,
nothing to install.

## Privacy promise

Nothing in this manual sends your files, email, or calendar data anywhere.
Every script runs locally on your computer. The only email that ever goes out
is one you choose to send yourself, using your own settings — nothing is
hardcoded. No API keys, no accounts, no secrets, no personal data in this
project.

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

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE` for the
full text.
