from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


deltas = {
    "U": Point(0, -1),
    "D": Point(0, 1),
    "L": Point(-1, 0),
    "R": Point(1, 0),
}


def chebyshev_distance(pos1: Point, pos2: Point) -> int:
    """Find the maximum difference on any axis between two positions."""
    return max(abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))


def follow(tail: Point, head_old: Point, head_new: Point) -> Point:
    """Compute the movement of the tail and return the new position."""

    # if the head has moved so that it's not touching anymore, just go where it was before
    if chebyshev_distance(tail, head_new) > 1:
        return head_old
    # otherwise, there's no need to move at all
    return tail


def main():
    head = Point(0, 0)
    tail = Point(0, 0)
    visited_by_tail = {tail}
    with open("inputs/day_09.txt") as f:
        for line in f:
            chunks = line.strip().split()
            delta = deltas[chunks[0]]
            times = int(chunks[1])

            for _ in range(times):
                new_head = head + delta
                tail = follow(tail, head, new_head)
                head = new_head
                visited_by_tail.add(tail)

    print("Part 1:", len(visited_by_tail))


if __name__ == '__main__':
    main()
