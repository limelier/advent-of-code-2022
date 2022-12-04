def contains(bigger_range, smaller_range):
    return bigger_range[0] <= smaller_range[0] and bigger_range[1] >= smaller_range[1]


def intersects(range1, range2):
    return range1[0] <= range2[0] <= range1[1] \
        or range1[0] <= range2[1] <= range1[1] \
        or contains(range2, range1)


count_contains = 0
count_intersections = 0
with open("inputs/day_04.txt", "r") as f:
    for line in f.readlines():
        left, right = line.strip().split(",")
        first_range = tuple(int(x) for x in left.split("-"))
        second_range = tuple(int(x) for x in right.split("-"))

        if contains(first_range, second_range) or contains(second_range, first_range):
            count_contains += 1
        if intersects(first_range, second_range):
            count_intersections += 1


print(count_contains)
print(count_intersections)

