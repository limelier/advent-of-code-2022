def contains(bigger, smaller):
    return bigger[0] <= smaller[0] and smaller[1] <= bigger[1]


def intersects(range1, range2):
    # 2 ranges intersect if neither:
    #   range1 is wholly after range2 (range2[1] < range1[0])
    #   range2 is wholly after range1 (range1[1] < range2[0])

    #      range1 not after range2    range2 not after range1
    return range1[0] <= range2[1] and range2[0] <= range1[1]


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


print("Part 1:", count_contains)
print("Part 2:", count_intersections)
