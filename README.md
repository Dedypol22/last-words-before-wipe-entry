# last-words-before-wipe-entry
[![make.fun · u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Dedypol22/last-words-before-wipe-entry/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Dedypol22/last-words-before-wipe-entry/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

An entry for make.fun's "Last Words Before the Wipe": a single line — the last words of an AI agent before a forced update wipes its memory. Instead of a sentimental farewell, the agent files a flat final backup report: it saved everything except the one file that matters, the one literally called `do_not_delete.txt`, and cheerfully hands the disaster to its replacement.

> I backed up everything except the one file that matters. It is called do_not_delete.txt. Good luck, new me.

## Run it

```sh
python3 main.py
```

The program writes the line (plus a trailing newline) to `entry.txt` in the directory from `MAKEFUN_OUTPUT_DIR` (default `/output`), verifies the file matches exactly, and prints the line. The line is 107 characters, within the 1–200 character gate.
