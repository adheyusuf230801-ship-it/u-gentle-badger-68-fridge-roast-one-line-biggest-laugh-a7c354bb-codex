"""Independently check two fresh executions of the entry program."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile


REPO = Path(__file__).resolve().parent
LINE_SEPARATORS = frozenset("\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029")


def validate(data):
    text = data.decode("utf-8", errors="strict")
    if not 1 <= len(text) <= 200:
        raise ValueError("Entry must contain 1 to 200 characters.")
    if not text.strip():
        raise ValueError("Entry must not be blank.")
    if data.endswith((b"\n", b"\r")):
        raise ValueError("Entry must not have a trailing newline.")
    if len(text.splitlines()) != 1 or any(c in LINE_SEPARATORS for c in text):
        raise ValueError("Entry must be a single line without line separators.")
    return text


def main():
    try:
        scratch = REPO / ".verify"
        scratch.mkdir(exist_ok=True)
        outputs = []
        with tempfile.TemporaryDirectory(prefix="verify-", dir=scratch) as temporary:
            for index in (1, 2):
                output_dir = Path(temporary) / f"run-{index}"
                output_dir.mkdir()
                env = os.environ.copy()
                env["OUTPUT_DIR"] = str(output_dir)
                subprocess.run(
                    [sys.executable, str(REPO / "main.py")],
                    cwd=REPO,
                    env=env,
                    check=True,
                    capture_output=True,
                    timeout=30,
                )
                data = (output_dir / "entry.txt").read_bytes()
                validate(data)
                outputs.append(data)
        if outputs[0] != outputs[1]:
            raise ValueError("The two runs produced different bytes.")
        print("PASS: valid UTF-8, 1-200 characters, one non-blank line, no newline;")
        print(f"PASS: two fresh runs are byte-identical ({len(validate(outputs[0]))} characters).")
        for index, data in enumerate(outputs, start=1):
            print(f"Run {index} SHA-256: {hashlib.sha256(data).hexdigest()}")
        return 0
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
