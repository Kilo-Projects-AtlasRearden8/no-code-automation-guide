#!/usr/bin/env python3
"""Tests for folder_watcher.py.

Run: python3 tests/test_folder_watcher.py
"""

import os
import sys
import tempfile
import threading
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import folder_watcher  # noqa: E402


def create_file_later(path, delay, content="arrived"):
    def _create():
        time.sleep(delay)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)

    thread = threading.Thread(target=_create, daemon=True)
    thread.start()
    return thread


def test_list_files_only_files():
    tmp = tempfile.mkdtemp()
    try:
        sub = os.path.join(tmp, "sub")
        os.makedirs(sub)
        with open(os.path.join(tmp, "a.txt"), "w") as fh:
            fh.write("a")
        with open(os.path.join(sub, "b.txt"), "w") as fh:
            fh.write("b")

        files = folder_watcher.list_files(tmp)
        assert "a.txt" in files
        assert "b.txt" not in files  # subfolder contents not listed
        assert "sub" not in files  # folders excluded
    finally:
        import shutil
        shutil.rmtree(tmp)


def test_watch_detects_new_file_without_logging_in_dry_run():
    tmp = tempfile.mkdtemp()
    try:
        log_path = os.path.join(tmp, "connections.log")
        with open(os.path.join(tmp, "existing.txt"), "w") as fh:
            fh.write("old")

        new_path = os.path.join(tmp, "new.txt")
        create_file_later(new_path, 0.05)

        # Watch long enough to catch the new file mid-poll.
        folder_watcher.watch_folder(tmp, dry_run=True, interval=0.01,
                                    max_polls=40, log_path=log_path)

        assert not os.path.exists(log_path), "dry-run must not write a log"
    finally:
        import shutil
        shutil.rmtree(tmp)


def test_watch_logs_new_file_when_apply():
    tmp = tempfile.mkdtemp()
    try:
        log_path = os.path.join(tmp, "connections.log")
        with open(os.path.join(tmp, "existing.txt"), "w") as fh:
            fh.write("old")

        new_path = os.path.join(tmp, "arrived.txt")
        create_file_later(new_path, 0.05)

        folder_watcher.watch_folder(tmp, dry_run=False, interval=0.01,
                                    max_polls=40, log_path=log_path)

        assert os.path.exists(log_path)
        with open(log_path, encoding="utf-8") as fh:
            content = fh.read()
        assert "arrived.txt" in content
        assert "new file:" in content
    finally:
        import shutil
        shutil.rmtree(tmp)


def test_watch_never_moves_or_deletes_files():
    tmp = tempfile.mkdtemp()
    try:
        with open(os.path.join(tmp, "keep.txt"), "w") as fh:
            fh.write("keep")
        folder_watcher.watch_folder(tmp, dry_run=False, interval=0.01,
                                    max_polls=2, log_path=os.path.join(tmp, "log.txt"))
        assert os.path.isfile(os.path.join(tmp, "keep.txt"))
    finally:
        import shutil
        shutil.rmtree(tmp)


if __name__ == "__main__":
    test_list_files_only_files()
    test_watch_detects_new_file_without_logging_in_dry_run()
    test_watch_logs_new_file_when_apply()
    test_watch_never_moves_or_deletes_files()
    print("All folder_watcher tests passed.")
