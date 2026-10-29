#!/usr/bin/env python3
"""Local-first folder watcher: a private app connection that never leaves your
computer.

Watches a folder and notes whenever a new file appears — like a personal,
local-only IFTTT applet. Defaults to dry-run: prints what it sees without
writing anything. With --apply, appends a line to connections.log (in the
folder you run the script from) each time a new file appears, with the file
name and time. It never moves, renames, or uploads anything. Press Ctrl-C to
stop.

Standard library only. No accounts, no API keys, no network, no secrets.
"""

import os
import sys
import time

DEFAULT_INTERVAL = 5  # seconds between polls
DEFAULT_MAX_POLLS = 0  # 0 means run until interrupted


def list_files(folder):
    """Return a set of file names (not folders) directly inside `folder`."""
    files = set()
    try:
        for entry in os.listdir(folder):
            path = os.path.join(folder, entry)
            if os.path.isfile(path):
                files.add(entry)
    except FileNotFoundError:
        print(f"Error: folder not found: {folder}", file=sys.stderr)
        sys.exit(1)
    return files


def append_log(message, log_path):
    """Append one line to the local connections log."""
    with open(log_path, "a", encoding="utf-8") as fh:
        fh.write(message + "\n")


def watch_folder(folder, dry_run=True, interval=DEFAULT_INTERVAL, max_polls=0,
                 log_path="connections.log"):
    """Poll `folder` for new files and log them when they appear."""
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        print(f"Error: not a directory: {folder}", file=sys.stderr)
        return 1

    log_name = os.path.basename(os.path.abspath(log_path))

    print(f"Watching: {folder}")
    print(f"Poll every {interval} second(s). Press Ctrl-C to stop.")
    if dry_run:
        print("Dry-run: nothing will be written to the log file.")
    else:
        print(f"Log file: {os.path.abspath(log_path)}")

    seen = list_files(folder)
    polls = 0

    try:
        while True:
            time.sleep(interval)
            current = list_files(folder)
            new_files = sorted(n for n in (current - seen) if n != log_name)

            if new_files:
                for name in new_files:
                    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} new file: {name}"
                    if dry_run:
                        print(f"[dry-run] {line}")
                    else:
                        append_log(line, log_path)
                        print(line)
                seen = current

            polls += 1
            if max_polls and polls >= max_polls:
                break
    except KeyboardInterrupt:
        print("\nStopped watching.")

    return 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)

    dry_run = True
    interval = DEFAULT_INTERVAL
    max_polls = DEFAULT_MAX_POLLS
    folder = None

    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in ("--apply", "-a"):
            dry_run = False
        elif arg in ("--dry-run", "-n"):
            dry_run = True
        elif arg in ("--interval", "-i") and i + 1 < len(argv):
            try:
                interval = float(argv[i + 1])
            except ValueError:
                print(f"Error: --interval must be a number, got: {argv[i + 1]}",
                      file=sys.stderr)
                return 1
            i += 1
        elif arg in ("--times", "-t") and i + 1 < len(argv):
            try:
                max_polls = int(argv[i + 1])
            except ValueError:
                print(f"Error: --times must be a number, got: {argv[i + 1]}",
                      file=sys.stderr)
                return 1
            i += 1
        elif arg in ("--log", "-l") and i + 1 < len(argv):
            log_path = argv[i + 1]
            i += 1
        elif not arg.startswith("-"):
            folder = arg
        else:
            print(f"Error: unknown option: {arg}", file=sys.stderr)
            return 1
        i += 1

    if folder is None:
        print("Usage: python3 folder_watcher.py <folder> [--apply] "
              "[--interval N] [--times M] [--log path]", file=sys.stderr)
        print("\nWatches <folder> and notes whenever a new file appears.")
        print("Defaults to dry-run: prints what it sees, writes nothing.")
        print("--apply   write new-file notes to connections.log (local file only)")
        print("\nSafety: never moves, renames, or uploads anything.")
        return 1

    return watch_folder(folder, dry_run=dry_run, interval=interval,
                        max_polls=max_polls)


if __name__ == "__main__":
    sys.exit(main())
