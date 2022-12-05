from typing import cast

# section assignment, effectively an int range with both ends inclusive
section = tuple[int, int]


def contains(outer: section, inner: section):
    return outer[0] <= inner[0] and inner[1] <= outer[1]


def intersects(section1: section, section2: section):
    # 2 sections intersect if neither section is wholly after the other
    # -> section1 not after section2 AND section2 not after section1
    return section1[0] <= section2[1] and section2[0] <= section1[1]

def main():
    count_contains = 0
    count_intersections = 0
    with open("inputs/day_04.txt", "r") as f:
        for line in f.readlines():
            left, right = line.strip().split(",")
            first_range = cast(section, tuple(int(x) for x in left.split("-")))
            second_range = cast(section, tuple(int(x) for x in right.split("-")))

            if contains(first_range, second_range) or contains(second_range, first_range):
                count_contains += 1
            if intersects(first_range, second_range):
                count_intersections += 1

    print("Part 1:", count_contains)
    print("Part 2:", count_intersections)


if __name__ == '__main__':
    main()
