#!/usr/bin/env python3
"""Tests for calendar_reminders.py.

Run: python3 tests/test_calendar_reminders.py
"""

import os
import sys
import tempfile
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import calendar_reminders  # noqa: E402


def write_reminders(tmp, lines):
    path = os.path.join(tmp, "reminders.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


def test_parse_reminders():
    tmp = tempfile.mkdtemp()
    try:
        today = date.today()
        soon = (today + timedelta(days=2)).isoformat()
        late = (today - timedelta(days=1)).isoformat()
        path = write_reminders(tmp, [
            "# comment",
            "Electric | " + soon + " | Pay electric",
            "Rent | " + late + " | Pay rent",
            "bad | not-a-date | x",  # skipped
            "Incomplete | 2026-11-05",  # skipped (<3 parts)
        ])
        reminders = calendar_reminders.parse_reminders(path)
        names = [r[0] for r in reminders]
        assert "Electric" in names
        assert "Rent" in names
        assert "bad" not in names
        assert "Incomplete" not in names
    finally:
        import shutil
        shutil.rmtree(tmp)


def test_categorize():
    today = date.today()
    reminders = [
        ("A", today, "msg A", 1),
        ("B", today + timedelta(days=3), "msg B", 2),
        ("C", today + timedelta(days=30), "msg C", 3),
        ("D", today - timedelta(days=2), "msg D", 4),
    ]
    due_today, upcoming, overdue = calendar_reminders.categorize(
        reminders, today, within_days=7)
    assert [r[0] for r in due_today] == ["A"]
    assert [r[0] for r in upcoming] == ["B"]
    assert [r[0] for r in overdue] == ["D"]


def test_mailto_uses_env_to_email():
    today = date.today()
    calendar_reminders.TO_EMAIL = "you@example.com"
    url = calendar_reminders.mailto("Dentist", "Dentist appointment", today)
    assert url.startswith("mailto:you@example.com?")
    assert "subject=Reminder%3A+Dentist+due" in url


def test_dry_run_prints_and_sends_nothing():
    tmp = tempfile.mkdtemp()
    try:
        today = date.today()
        soon = (today + timedelta(days=1)).isoformat()
        path = write_reminders(tmp, ["Reminder | " + soon + " | Do it"])
        calendar_reminders.check_reminders(path, within_days=7, today=today,
                                           dry_run=True)
    finally:
        import shutil
        shutil.rmtree(tmp)


def test_no_reminders_handled_gracefully():
    tmp = tempfile.mkdtemp()
    try:
        path = write_reminders(tmp, [])
        assert calendar_reminders.check_reminders(path, dry_run=True) == 0
    finally:
        import shutil
        shutil.rmtree(tmp)


if __name__ == "__main__":
    test_parse_reminders()
    test_categorize()
    test_mailto_uses_env_to_email()
    test_dry_run_prints_and_sends_nothing()
    test_no_reminders_handled_gracefully()
    print("All calendar_reminders tests passed.")
