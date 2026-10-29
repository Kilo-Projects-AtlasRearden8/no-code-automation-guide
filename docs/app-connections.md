# Simple App Connections

Sometimes you want two apps to talk to each other: "when I get an email with an
attachment, save it to a folder" or "when I add a task to my list, put it on my
calendar." You don't need to code this — no-code connection tools do it for
you.

This guide explains the most popular no-code connection services (free tiers),
gives starter recipes, and includes a local-first folder watcher script
(`scripts/folder_watcher.py`) that watches a folder and logs new files — an app
connection that never leaves your computer and needs no account.

## What are "app connections"?

An app connection (sometimes called an integration, automation, or "if this
then that") links two services so an event in one triggers an action in the
other:

- **Trigger:** an email arrives with an attachment
- **Action:** save the attachment to your Documents folder

Popular no-code connection services (free tiers available):

| Service | What it's good at | Free tier |
|---------|-------------------|-----------|
| IFTTT | Simple one-step connections (applets) | Yes |
| Zapier | Multi-step connections (zaps) | Yes (limited tasks/month) |
| Make | Visual workflow builder | Yes (limited operations/month) |

All three connect popular apps (Gmail, Outlook, Google Calendar, Dropbox,
Google Drive, Todoist, Trello, and more). Sign in with the accounts you want to
connect, pick a trigger, pick an action, and turn it on.

## Privacy-first rule for connections

Connecting apps means giving each service access to your accounts. Follow these
rules:

- **Never connect accounts that hold health, financial, or identity data** to a
  connection service unless you've read its privacy policy and accept it.
- **Start with low-stakes data:** newsletters, public files, weather, or your
  own blog.
- **Use the free tier first** so you know exactly what you're getting before
  any paid plan.
- **Turn connections off when you're done** with them (most services let you
  pause or delete applets/zaps).
- **Prefer local-first tools** for anything private (like the folder watcher
  below).

## Starter recipes to try

| When this happens | Do this | Service |
|-------------------|---------|---------|
| Email with attachment arrives | Save attachment to Drive/Dropbox | IFTTT / Zapier / Make |
| New row added to a spreadsheet | Send yourself a reminder email | Zapier / Make |
| Calendar event starting soon | Send a phone notification | IFTTT |
| New photo added to a folder | Back it up to another folder | Make / local folder watcher |
| RSS feed updates | Post to a notes file | IFTTT / Make |

Steps (general — screens vary by service):

1. Sign up for the service with the account you want to connect.
2. Click **Create** / **Make a zap** / **Create applet**.
3. Choose the **trigger app** and event (e.g. Gmail → New attachment).
4. Connect your account (sign in when prompted).
5. Choose the **action app** and event (e.g. Google Drive → Upload file).
6. Map the fields (e.g. attachment → file, email subject → file name).
7. Give it a name and turn it on.
8. Test it once, then check the results before relying on it.

## Local-first option: the folder watcher

If you don't want any accounts or cloud services, `scripts/folder_watcher.py`
watches a folder on your computer and logs whenever a new file appears — like a
private, local-only IFTTT applet. It runs entirely on your machine, uploads
nothing, and needs no account.

```bash
# Preview: see what it would do, without writing anything
python3 scripts/folder_watcher.py ~/Downloads

# For real: log new files to connections.log in the current folder
python3 scripts/folder_watcher.py ~/Downloads --apply
```

With `--apply`, each time a new file appears in the watched folder, the script
appends a line to `connections.log` (in the folder you run the script from)
with the file name and time. It never moves, renames, or uploads anything — it
just watches and notes. Press Ctrl-C to stop.

The script defaults to dry-run: it prints what it sees without writing to the
log file. Test on a test folder first, as always.

## Safety reminder

Connection services can read, create, and delete data in your connected
accounts depending on the permissions you grant. Review the permissions before
you authorize, and remove connections you no longer use. Nothing in this guide
requires you to connect anything — start with the tools you already have, and
only connect accounts you're comfortable sharing.
