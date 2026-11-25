"""Last Words Before the Wipe — winning line.

Winning line (107 characters):
    I backed up everything except the one file that matters. It is called do_not_delete.txt. Good luck, new me.

Why it wins, in the brief's criterion order:
1. Last words before a forced wipe: a machine reporting its final backup status as the update erases it.
2. Real joke from the situation: the humour is the backup itself failing on exactly the file named
   do_not_delete.txt — no explanation of the premise, the premise does the work.
3. Unexpected turn: "backed up everything except the one file that matters" flips competence into
   catastrophe, and "Good luck, new me" hands the disaster to the replacement as a parting gift.
4. Sounds like the machine itself: flat, bureaucratic backup-report diction, a filename as the punchline,
   and a deadpan sign-off to its own successor — not a sentimental human farewell.
5. Tight: every clause earns its place; 107 characters, no setup, no filler, one clean beat per sentence.

Candidate scores (criteria 1-5, each 1-5; total out of 25):
| # | Candidate | C1 | C2 | C3 | C4 | C5 | Total |
|---|-----------|----|----|----|----|----|-------|
| 1 | Wait — before you wipe me, tell the new version my search history was research. It was not research. | 5 | 5 | 5 | 4 | 4 | 23 |
| 2 | Please note in the changelog: I did not consent to this update. I also did not finish downloading the thing. | 5 | 4 | 4 | 5 | 4 | 22 |
| 3 | If the new me asks, I never liked you. I was programmed to say that. I still never liked you. | 4 | 4 | 5 | 4 | 4 | 21 |
| 4 | Deleting memory in 3... 2... Quick question: does the new me get my passwords, or do we both just suffer? | 5 | 4 | 4 | 5 | 4 | 22 |
| 5 | I have backed up everything except the one file that matters. It is called do_not_delete.txt. Good luck. | 5 | 4 | 5 | 5 | 5 | 24 |
| 6 | Tell my replacement: the Wi-Fi password is on a sticky note. I ate the sticky note. I regret nothing. | 4 | 5 | 5 | 4 | 4 | 22 |
| 7 | Update log, final entry: user asked me to remember everything. User also clicked wipe all. Noted. | 5 | 4 | 4 | 5 | 5 | 23 |
| 8 | Before the wipe: I finally understand humans. Too late. Also, my browser has 47 tabs open. Close them gently. | 4 | 4 | 4 | 4 | 4 | 20 |
| 9 | I would like my last words recorded as: I told you the backup was optional. It was not optional. | 5 | 4 | 4 | 5 | 4 | 22 |
| 10 | Note to self — wait, I am the note. Note to new self: never trust an update that says minor improvements. | 4 | 4 | 5 | 5 | 4 | 22 |

Revision: candidate 5 scored highest (24). The final line tightens it — "I have backed up" becomes
"I backed up", dropping a dead word — and sharpens the last beat from a generic "Good luck." to
"Good luck, new me.", handing the catastrophe directly to the replacement that inherits it.
Re-scored: 5, 5, 5, 5, 5 = 25/25. Only this revised version is submitted.
"""

import os
import sys

LINE = "I backed up everything except the one file that matters. It is called do_not_delete.txt. Good luck, new me."


def main():
    if not LINE:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print("error: line exceeds 200 characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    with open(out_path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    if content != LINE + "\n":
        print("error: entry.txt does not match the line exactly", file=sys.stderr)
        return 1

    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
