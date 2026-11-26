"""Write the deterministic Fridge Roast entry using only the standard library."""

import os
from pathlib import Path


ENTRY = "My smart fridge can describe ice in 40 languages. I'd settle for it in a glass."
LINE_SEPARATORS = frozenset("\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029")


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("Entry must contain 1 to 200 characters.")
    if not ENTRY.strip() or any(char in LINE_SEPARATORS for char in ENTRY):
        raise ValueError("Entry must be one non-blank line without line separators.")

    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
