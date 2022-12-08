from enum import Enum
from functools import reduce
from operator import mul
from typing import Iterable

input_lines = open("inputs/day_08/day_08.txt").readlines()
# input_lines = open("inputs/day_08/example.txt").readlines()
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


def trees_visible(row: int, col: int, direction: Direction) -> int:
    """Count the number of trees visible from the tree at the given ``row`` and ``col``"""
    return count_visible(tree_map[row][col], trees_to_edge(row, col, direction))


def all_trees_visible(row: int, col: int) -> dict[Direction, int]:
    """Return count of trees visible in all 4 directions."""
    return dict((direction, trees_visible(row, col, direction)) for direction in Direction)


def visible_from_outside(row: int, col: int) -> bool:
    tree = tree_map[row][col]
    return all(tree_map[r][col] < tree for r in range(0, row)) \
        or all(tree_map[r][col] < tree for r in range(row + 1, rows)) \
        or all(tree_map[row][c] < tree for c in range(0, col)) \
        or all(tree_map[row][c] < tree for c in range(col + 1, cols))


def scenic_score(row: int, col: int) -> int:
    return reduce(mul, all_trees_visible(row, col).values())


def main():
    num_visible = len([
        # print(row, col, tree_map[row][col])
        (row, col)
        for row in range(1, rows - 1)
        for col in range(1, cols - 1)
        if visible_from_outside(row, col)
    ]) + 2 * rows + 2 * (cols - 2)
    print("Part 1:", num_visible)

    best_scenic_score = max(
        scenic_score(row, col)
        for row in range(1, rows - 1)
        for col in range(1, cols - 1)
    )
    print("Part 2:", best_scenic_score)


if __name__ == '__main__':
    main()
