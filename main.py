"""Write the phone battery's last text message to its charger.

One line of plain text, at most 200 characters, written to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13, standard library only, no network.
"""

import os

# The battery's last text to the charger it waited for all day.
# 137 characters. The joke turns on the last words: after a day of
# waiting to be plugged in, the battery confesses it never loved the
# charger at all — it was always the power bank.
LINE = (
    "I waited all day for you to plug me in, and now I'm at 1%. "
    "Goodbye \u2014 and for the record, I never loved you. "
    "It was always the power bank."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not start or end with space"
    assert "\u2014" in LINE, "the em dash is part of the line's voice"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
