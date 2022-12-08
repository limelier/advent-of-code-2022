from enum import Enum
from functools import reduce
from operator import mul
from typing import Iterable

# COMMON FOR PART 1 AND 2 ##############################################################

input_lines = open("inputs/day_08/day_08.txt").readlines()
tree_map = [[int(c) for c in line.strip()] for line in input_lines]

rows = len(tree_map)
cols = len(tree_map[0])


class Direction(Enum):
    UP, DOWN, LEFT, RIGHT = range(4)


def trees_to_edge(row: int, col: int, direction: Direction) -> Iterable[int]:
    """
    Return a sequence of all heights of trees located in the given ``direction`` from the tree at ``(row, col)``,
    in order of closest to farthest.
    """
    match direction:
        case Direction.UP:
            return (tree_map[r][col] for r in reversed(range(0, row)))
        case Direction.DOWN:
            return (tree_map[r][col] for r in range(row + 1, rows))
        case Direction.LEFT:
            return (tree_map[row][c] for c in reversed(range(0, col)))
        case Direction.RIGHT:
            return (tree_map[row][c] for c in range(col + 1, cols))


def trees_visible(row: int, col: int, direction: Direction) -> int:
    """Count the number of trees visible from the tree at the given ``row`` and ``col``"""
    return count_visible(tree_map[row][col], trees_to_edge(row, col, direction))


def all_trees_visible(row: int, col: int) -> dict[Direction, int]:
    """Get count of trees visible in all 4 directions."""
    return dict((direction, trees_visible(row, col, direction)) for direction in Direction)


# PART 1 ##############################################################

def part_1() -> int:
    """Get the number of trees in the forest that are visible from outside it."""
    return len([
        # print(row, col, tree_map[row][col])
        (row, col)
        for row in range(1, rows - 1)
        for col in range(1, cols - 1)
        if visible_from_outside(row, col)
    ]) + 2 * rows + 2 * (cols - 2)


def outside_visible(row: int, col: int, direction: Direction) -> bool:
    """Check if a tree at the given coordinates can 'see' the outside in the given direction."""
    return all(tree < tree_map[row][col] for tree in trees_to_edge(row, col, direction))


def visible_from_outside(row: int, col: int) -> bool:
    """Check if a tree at the given coordinates is visible from the outside."""
    return any(outside_visible(row, col, direction) for direction in Direction)


# PART 2 ##############################################################

def count_visible(origin_tree: int, line_of_trees: Iterable[int]) -> int:
    """
    Count the number of trees in the line, starting from 0, visible from the origin tree.
    :param origin_tree: height of origin tree
    :param line_of_trees: height of trees to check, ordered closest to farthest
    :return: number of trees visible up to and including the first tree as tall or taller than the origin tree
    """
    i = 0
    for (i, tree) in enumerate(line_of_trees):
        if tree >= origin_tree:
            return i + 1
    return i + 1


def scenic_score(row: int, col: int) -> int:
    """Get the 'scenic score' of the tree at the given coordinates."""
    return reduce(mul, all_trees_visible(row, col).values())


def part_2() -> int:
    """Get the highest 'scenic score' in the forest."""

    # no need to consider outside trees, they cannot win over inside ones
    return max(
        scenic_score(row, col)
        for row in range(1, rows - 1)
        for col in range(1, cols - 1)
    )


# COMMON AGAIN ############################################################

def main():
    print("Part 1:", part_1())
    print("Part 2:", part_2())


if __name__ == '__main__':
    main()
