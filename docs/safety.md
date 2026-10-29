# Safety First

Before you automate anything, read this page. It takes two minutes and it will
save you from headaches later.

## The golden rules

1. **Test on copies, never move originals.** Every script in this manual works
   on a copy of your files by default. Run it on a test folder first. Only point
   it at your real files once you're sure it does what you expect.
2. **Scripts preview before they act.** Every script defaults to dry-run mode:
   it shows you what it *would* do without changing anything. You opt in to
   making changes (with `--apply`), never by accident.
3. **You can read every script.** These are tiny Python scripts (under 100
   lines each). Open them, read them, and only run them when you understand
   what they do.
4. **Start small.** Automate one folder, one task, one afternoon. Don't try to
   organize your whole computer in one sitting.
5. **Nothing leaves your computer.** No script uploads your files, email, or
   calendar data. The only email that ever goes out is one you choose to send
   yourself, using your own settings.

## Why we test on copies

If a script has a bug, you want it to scramble a test folder, not your only
copy of last year's tax documents. A copy costs nothing; your originals are
irreplaceable.

## How to make a test copy

On Windows, copy your folder (e.g. Downloads) to `Downloads Test`.
On Mac, right-click the folder → Duplicate.
On Linux, `cp -r Downloads Downloads-Test`.

Point the script at the test copy first. Check the results. Then decide whether
to run it on the real folder.

## What these scripts do NOT do

- They do not send your files anywhere. Everything stays on your computer.
- They do not require API keys, accounts, or personal information.
- They do not delete anything unless you explicitly opt in.
- No credentials or secrets are stored in this project.
- Calendar reminders and app connections stay local; nothing is posted to the
  web.

If a script ever asks for something that makes you uncomfortable, stop and read
the source. You're in control.
