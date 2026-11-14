#!/usr/bin/env python3
"""Append today's date to activity.log and commit it."""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "activity.log"


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def main() -> int:
    today = dt.date.today().isoformat()
    lines = LOG.read_text(encoding="utf-8").splitlines() if LOG.exists() else []

    if today in lines:
        print(f"{today} already logged, nothing to commit")
        return 0

    lines.append(today)
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")

    git("add", "activity.log")
    git("commit", "-m", f"log: {today}")
    print(f"committed log: {today}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
