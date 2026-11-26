"""The 3AM Commit Message.

The joke: after a night of chasing a Heisenbug that only appears when no
one is looking, the exhausted agent stops debugging and starts fearing
the bug. "It knows. It waits." turns a flaky test into a stalker, and the
punchline ("before it learns my name") is the agent fleeing to bed while
it still has the chance. It reads like a real commit typed at 3am by
something that has been awake far too long: flat, paranoid, and done.
Three short sentences, escalating dread, zero explanation of the fix,
because there was no fix, only surrender and a bedtime.
"""

import os

LINE = (
    "fix: the bug only reproduces when nobody is watching. "
    "it knows. it waits. i am going to bed before it learns my name"
)


def write_entry(out_dir):
    """Write LINE to entry.txt as bytes, no trailing newline, mode 0644."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
