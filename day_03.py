import string


def priority(item):
    return string.ascii_letters.index(item) + 1


part1_sum = 0
part2_sum = 0

group_of_three = []
with open("inputs/day_03.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()

        # part 1
        split_point = len(line) // 2

        first_compartment = line[:split_point]
        second_compartment = line[split_point:]

        first_compartment_items = set(first_compartment)
        second_compartment_items = set(second_compartment)

        common = first_compartment_items.intersection(second_compartment_items).pop()
        part1_sum += priority(common)

        # part 2
        group_of_three.append(set(line))
        if len(group_of_three) == 3:
            badge = set.intersection(*group_of_three).pop()
            part2_sum += priority(badge)
            group_of_three = []

print("Part 1:", part1_sum)
print("Part 2:", part2_sum)
