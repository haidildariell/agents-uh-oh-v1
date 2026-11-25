#!/usr/bin/env python3
"""The Agent's Uh-Oh - entry: writes the agent's honest blurt to /output/entry.txt."""

import os

def get_word():
    """Return the agent's honest blurt: one token, no spaces."""
    word = "underthinking"
    if not word or " " in word or "\n" in word:
        raise ValueError("word must be a single token")
    return word


def main():
    word = get_word()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
