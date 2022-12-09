from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


move_deltas = {
    "U": Point(0, -1),
    "D": Point(0, 1),
    "L": Point(-1, 0),
    "R": Point(1, 0),
}


def chebyshev_distance(pos1: Point, pos2: Point) -> int:
    """Find the maximum difference on any axis between two positions."""
    return max(abs(pos1.x - pos2.x), abs(pos1.y - pos2.y))


def clamp(num: int, lower: int, upper: int) -> int:
    """Clamp an integer within an inclusive interval."""

    if num < lower:
        return lower
    if num > upper:
        return upper
    return num


def clamp_delta(delta: Point) -> Point:
    """Clamp a delta to only adjacent orthogonal or diagonal movements."""
    return Point(clamp(delta.x, -1, 1), clamp(delta.y, -1, 1))


def follow(tail: Point, head: Point) -> Point:
    """Compute the movement of the tail and return the new position."""

    if chebyshev_distance(tail, head) > 1:  # not touching
        return tail + clamp_delta(head - tail)

    return tail


def main():
    head = Point(0, 0)
    tail = Point(0, 0)
    visited_by_tail = {tail}
    with open("inputs/day_09.txt") as f:
        for line in f:
            chunks = line.strip().split()
            delta = move_deltas[chunks[0]]
            times = int(chunks[1])

            for _ in range(times):
                head += delta
                tail = follow(tail, head)
                visited_by_tail.add(tail)

    print("Part 1:", len(visited_by_tail))


if __name__ == '__main__':
    main()
