import string


def priority(item):
    return string.ascii_letters.index(item) + 1


# part 1 - add up priorities of items that appear in both 1st and 2nd half of backpacks
def part_1(rucksack):
    split_point = len(rucksack) // 2
    first_compartment_items = set(rucksack[:split_point])
    second_compartment_items = set(rucksack[split_point:])
    common = set.intersection(first_compartment_items, second_compartment_items).pop()
    return priority(common)


# part 2 - add up priorities of common item in every group of 3 rucksacks
def part_2(rucksacks):
    badge = set.intersection(*rucksacks).pop()
    return priority(badge)


def main():
    sum_1 = 0
    sum_2 = 0

    group_of_three = []
    with open("inputs/day_03.txt", "r") as f:
        for line in f.readlines():
            rucksack = line.strip()

            sum_1 += part_1(rucksack)

            group_of_three.append(set(rucksack))
            if len(group_of_three) == 3:
                sum_2 += part_2(group_of_three)
                group_of_three = []

    print("Part 1:", sum_1)
    print("Part 2:", sum_2)


if __name__ == '__main__':
    main()
