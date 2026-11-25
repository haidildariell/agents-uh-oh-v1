"""The Agent's Uh-Oh entry.

Writes the agent's one-word confession to /output/entry.txt.
No network, no dependencies, no arguments.
"""

import os

WORD = "underthinking"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
