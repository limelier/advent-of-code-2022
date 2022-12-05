import re
from copy import deepcopy

move_line_pattern = re.compile(r"move (?P<n>\d+) from (?P<src>\d+) to (?P<dst>\d+)")

stacks_1 = [
    list(line.strip())
    for line in open("inputs/day_05/stacks.txt", "r").readlines()
]
stacks_2 = deepcopy(stacks_1)


def move_9000(n, src, dst):
    for _ in range(n):
        stacks_1[dst - 1].append(stacks_1[src - 1].pop())


def move_9001(n, src, dst):
    moved = stacks_2[src - 1][-n:]
    del(stacks_2[src - 1][-n:])
    stacks_2[dst - 1] += moved


def tops(stacks):
    return "".join([stack[-1] for stack in stacks])


def main():
    with open("inputs/day_05/moves.txt", "r") as f:
        for line in f.readlines():
            groups = move_line_pattern.match(line.strip()).groups()
            n, src, dst = (int(group) for group in groups)
            move_9000(n, src, dst)
            move_9001(n, src, dst)

    print("Part 1:", tops(stacks_1))
    print("Part 2:", tops(stacks_2))


if __name__ == '__main__':
    main()
