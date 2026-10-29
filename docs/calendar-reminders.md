# Calendar Reminders

Never forget an appointment, a bill, or a library book again. Calendar
reminders live in your calendar app and nudge you when something is coming up
— no code, no new account needed.

This guide covers two approaches: the built-in reminders in your calendar app,
and a tiny local script (`scripts/calendar_reminders.py`) that reads a plain
text reminders file on your own computer and tells you what's due today,
coming up soon, or already overdue.

## Option 1: Your calendar app (no code at all)

### Google Calendar
1. Open calendar.google.com (or the Google Calendar app).
2. Create an event (e.g. "Dentist appointment").
3. Click **Add notification** and choose when to be reminded (10 minutes, 1
   hour, 1 day, or a custom time before).
4. Set it to repeat if it's a recurring thing (weekly meds, monthly bill).
5. Make sure notifications are on for the calendar (phone/desktop).

### Outlook Calendar
1. Open the event, then find **Reminder** (or "Remind me").
2. Pick when you want to be notified.
3. For repeating items, set **Repeat** (daily, weekly, monthly) and choose an
   end date or "never."

### Apple Calendar (Mac / iPhone)
1. Open the event, then click or tap **calendar** → **alert**.
2. Choose when to be reminded (at time of event, 5 minutes before, 1 day
   before, custom).
3. Set **Repeat** for recurring events.

## Option 2: The local reminders script

`scripts/calendar_reminders.py` reads a `reminders.txt` file you maintain and
tells you which reminders are due today, coming up soon, or already overdue —
all on your own computer, no apps or accounts needed.

A sample `reminders.txt` looks like this:

```
# Reminder name | due date (YYYY-MM-DD) | message
Electric bill | 2026-11-05 | Pay the electric bill
Library books | 2026-11-10 | Return library books
Dentist | 2026-11-01 | Dentist appointment
```

Lines starting with `#` are comments and ignored. The date format is
year-month-day (2026-11-05).

### Step 1: Create your reminders file

Create `reminders.txt` somewhere easy to find, like your Documents folder:

```
# My reminders
Electric bill | 2026-11-05 | Pay the electric bill
Library books | 2026-11-10 | Return library books
```

Use real dates. The date format is year-month-day (2026-11-05).

### Step 2: Run the reminder check (dry run)

```bash
python3 scripts/calendar_reminders.py ~/Documents/reminders.txt
```

You'll see what's due today, upcoming within 7 days, and overdue — plus a
`mailto:` link for each one you can click to email yourself.

### Step 3: Send email for real (optional)

To actually send email, set these environment variables in your shell (never in
this project), then run with `--apply`:

```
export SMTP_HOST=smtp.example.com
export SMTP_USER=you@example.com
export SMTP_PASS=your-app-password
export FROM_EMAIL=you@example.com
export TO_EMAIL=you@example.com

python3 scripts/calendar_reminders.py ~/Documents/reminders.txt --apply
```

No credentials are stored in this script or the repo. `--apply` sends nothing
unless all SMTP variables are set.

## Make it a habit

A reminder only works if you look at it. Pick a regular time — every morning
with coffee, or every Sunday evening — and run the check or glance at your
calendar. You can also set a repeating event called "Check reminders" so your
calendar reminds you to check your reminders.

## Privacy

All reminder data stays in `reminders.txt` on your computer. Nothing is
uploaded. Do not commit `reminders.txt` — it contains your personal data. It's
already ignored by `.gitignore`.

Calendar reminders are an organizational tool, not financial or medical advice.
