"""The Robot Vacuum's Best Excuse: writes the entry to /output/entry.txt."""

from pathlib import Path

LINE = "My cliff sensor saw the rug's shadow, panicked, and filed the whole corner as a staircase."


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
