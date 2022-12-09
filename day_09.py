from __future__ import annotations

from dataclasses import dataclass


def clamp(num: int, lower: int, upper: int) -> int:
    """Clamp an integer within an inclusive interval."""

    if num < lower:
        return lower
    if num > upper:
        return upper
    return num


@dataclass(frozen=True)
class Vec2:
    x: int
    y: int

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def clamp_unit(self: Vec2) -> Vec2:
        """Clamp a Vec2 to the square between (-1, -1) and (1, 1)."""
        return Vec2(clamp(self.x, -1, 1), clamp(self.y, -1, 1))


move_deltas = {
    "U": Vec2(0, -1),
    "D": Vec2(0, 1),
    "L": Vec2(-1, 0),
    "R": Vec2(1, 0),
}


class Point(Vec2):
    @staticmethod
    def of_vec2(vec2: Vec2):
        return Point(vec2.x, vec2.y)

    def chebyshev(self, other: Point):
        """Get the maximum difference on any axis between two positions."""
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def moved(self, delta: Vec2) -> Point:
        """Get a copy of this point moved by ``delta``."""
        return Point.of_vec2(self + delta)

    def dragged_towards(self, other: Point) -> Point:
        """Get a copy of this point dragged towards the other by at most 1 unit orthogonally or diagonally."""
        if self.chebyshev(other) > 1:  # not 'touching' other, need to move
            return self.moved((other - self).clamp_unit())
        return self


@dataclass
class Rope:
    points: list[Point]

    @staticmethod
    def over_origin(length: int):
        return Rope([Point(0, 0)] * length)

    @property
    def head(self):
        return self.points[0]

    @property
    def tail(self):
        return self.points[-1]

    def move_head(self, delta: Vec2) -> Rope:
        """Move head by a certain delta, and drag the rest of the rope behind it."""
        new_points = [self.head.moved(delta)]
        for point in self.points[1:]:
            new_points.append(point.dragged_towards(new_points[-1]))
        return Rope(new_points)


class RopeStateMachine:
    def __init__(self, rope_len: int):
        self.rope = Rope.over_origin(rope_len)
        self.visited_by_tail = {self.rope.tail}

    def move(self, delta: Vec2):
        """Move the head of the rope by delta, recording the new tail position."""
        self.rope = self.rope.move_head(delta)
        self.visited_by_tail.add(self.rope.tail)


def main():
    part_1 = RopeStateMachine(2)
    part_2 = RopeStateMachine(10)
    with open("inputs/day_09.txt") as f:
        for line in f:
            chunks = line.strip().split()
            delta = move_deltas[chunks[0]]
            times = int(chunks[1])

            for _ in range(times):
                part_1.move(delta)
                part_2.move(delta)

    print("Part 1:", len(part_1.visited_by_tail))
    print("Part 2:", len(part_2.visited_by_tail))


if __name__ == '__main__':
    main()
