from typing import Iterator


def tick_addition() -> Iterator[int]:
    """Yield delta for register X in each tick."""
    with open("inputs/day_10/day_10.txt", "r") as f:
        for line in f.readlines():
            chunks = line.strip().split()

            match chunks:
                case ["noop"]:
                    yield 0
                case ["addx", num]:
                    yield 0
                    yield int(num)


x = 1  # sprite middle; sprite is (x-1, x, x+1)
signal_strengths_sum = 0
bitmap = [[False] * 40 for _ in range(6)]
bitmap_target = 0
for i, delta in enumerate(tick_addition()):
    tick = i + 1
    # part 1
    if (tick - 20) % 40 == 0:
        signal_strengths_sum += x * tick

    # part 2
    row, col = bitmap_target // 40, bitmap_target % 40
    if x - 1 <= col <= x + 1:  # sprite overlaps target
        bitmap[row][col] = True

    bitmap_target += 1
    x += delta

print("Part 1:", signal_strengths_sum)
print("Part 2:")
for bitmap_row in bitmap:
    print("".join("██" if bit else "░░" for bit in bitmap_row))
