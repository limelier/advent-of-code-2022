import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# convention: all points are (y, x) = (row, col)
# preamble
def char_to_heightmap(c):
    if c == "S":
        c = "a"
    if c == "E":
        c = "z"
    return ord(c) - ord("a")


chars = np.array([
    list(line.strip())
    for line in open("inputs/day_12.txt")
])

start = np.where(chars == "S")
start = (start[0][0], start[1][0])
end = np.where(chars == "E")
end = (end[0][0], end[1][0])

z = np.array([
    [char_to_heightmap(c) for c in line]
    for line in chars
])


# solving the problem
def heuristic(point) -> int:
    """Calculate Manhattan distance to goal as an A* heuristic."""
    return np.abs(np.array(point) - np.array(end)).sum()


def reconstruct_path(beginning, came_from):
    path = [end]
    while path[0] != beginning:
        path.insert(0, came_from[path[0]])
    return path


def accessible(point):
    deltas = [np.array(x) for x in [[1, 0], [-1, 0], [0, 1], [0, -1]]]
    # all orthogonal neighbors
    neighbors = [np.array(point) + delta for delta in deltas]
    # filter only those in bounds
    real_neighbors = [
        n for n in neighbors
        if (np.array([0, 0]) <= n).all() and (n < z.shape).all()
    ]
    # filter only those at most 1 higher
    return [tuple(n) for n in real_neighbors if z[tuple(n)] - z[tuple(point)] <= 1]


def a_star(beginning):
    # length of the shortest known path start->point
    g_score = {beginning: 0}
    # estimate of the shortest path start->point->end
    f_score = {beginning: heuristic(beginning)}
    # previous node in the shortest known path start->point
    came_from = {}

    to_visit = set()
    to_visit.add(beginning)
    while len(to_visit) > 0:
        current = to_visit.pop()
        if current == end:
            return reconstruct_path(beginning, came_from)

        for neighbor in accessible(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                to_visit.add(neighbor)


path = np.array(a_star(start))
# this is terribly inefficient but i don't care anymore
# best_path = min((np.array(a_star((y, 0))) for y in range(z.shape[0])), key=lambda p: len(p))
print("Part 1:", len(path) - 1)
# print("Part 2:", len(best_path) - 1)

# pretty plots

plt.figure(figsize=(15, 4.5))

sns.heatmap(
    data=z,
    cmap="terrain",
    vmin=-10,
    vmax=26,
    xticklabels=False,
    yticklabels=False,
    cbar=False,
)
# plt.plot(best_path[:, 1] + .5, best_path[:, 0] + .5, "b")
plt.plot(path[:, 1] + .5, path[:, 0] + .5, "r")
plt.plot(start[1] + .5, start[0] + .5, "kx")
# plt.plot(best_path[0][1] + .5, best_path[0][0] + .5, "kx")
plt.plot(end[1] + .5, end[0] + .5, "rx")

plt.axis("scaled")
plt.tight_layout()
plt.show()
