# Day 1
all_sums = []
with open("inputs/day_01.txt", "r") as f:
    current_sum = 0
    for line in f.readlines():
        line = line.strip()
        if line == "":
            all_sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    all_sums.append(current_sum)

# Part 1
print("Part 1:", max(all_sums))

# Part 2
print("Part 2:", sum(sorted(all_sums)[-3:]))
