import re
from copy import deepcopy

stacks = [list(line.strip()) for line in open("inputs/day_05_stacks", "r").readlines()]
stacks_2 = deepcopy(stacks)


def move(n, src, dst):
    for _ in range(n):
        stacks[dst - 1].append(stacks[src - 1].pop())


def move_9001(n, src, dst):
    moved = stacks_2[src - 1][-n:]
    stacks_2[src - 1] = stacks_2[src - 1][:-n]
    stacks_2[dst - 1] += moved


move_line_pattern = re.compile(r"move (?P<n>\d+) from (?P<src>\d+) to (?P<dst>\d+)")

with open("inputs/day_05_moves", "r") as f:
    for line in f.readlines():
        matches = move_line_pattern.match(line.strip())
        n = int(matches.group("n"))
        src = int(matches.group("src"))
        dst = int(matches.group("dst"))
        move(n, src, dst)
        move_9001(n, src, dst)

tops = "".join([stack[-1] for stack in stacks])
tops_2 = "".join([stack[-1] for stack in stacks_2])
print(tops)
print(tops_2)
