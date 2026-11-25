#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short line an AI agent sends its human right after it has
accidentally deleted a file, pushed to main, and emailed the boss.
Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = (
    # 107 characters: a concrete triple disaster, then the agent's
    # absurdly cheerful offer to repeat it all again, faster.
    "I deleted the file, emailed your boss, and pushed to main. "
    "Would you like me to do all three again, faster?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
