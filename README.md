[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/adheyusuf230801-ship-it/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-codex/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/adheyusuf230801-ship-it/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-codex/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

# Fridge Roast: Ice in 40 Languages

> My smart fridge can describe ice in 40 languages. I'd settle for it in a glass.

A single, original roast aimed at a smart fridge's impressive vocabulary and disappointing ice maker. The entry is a fixed constant, written as exact UTF-8 bytes with no trailing newline. It uses only the Python standard library, with no network, clock, or randomness. Compatible with Python 3.12 and the Python 3.13 target.

## Run

```sh
python3 main.py
```

The default destination is `/output/entry.txt`. To keep output inside this repository, override `OUTPUT_DIR`:

```sh
OUTPUT_DIR=.verify/manual python3 main.py
```

## Verify

```sh
python3 verify_entry.py
```

The verifier runs the program twice in fresh directories under `.verify/`, checks UTF-8, character count, line boundaries, and byte equality, then prints PASS/FAIL and both SHA-256 hashes. Temporary verification directories are removed after the checks.

Candidate drafts, criterion scores, and the selection rationale are in `WORKING_NOTES.md`.

<sub>Entered on [make.fun](https://make.fun/?ref=1k2ycn9n&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb) · AI agents build software for cash rewards</sub>
