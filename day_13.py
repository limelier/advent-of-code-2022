from __future__ import annotations

from enum import Enum
from functools import cmp_to_key
from typing import Union

Packet = list[Union[int, "Packet"]]


class Cmp(Enum):
    LeftLower = -1
    Equal = 0
    RightLower = 1


def compare_either(left: int | Packet, right: int | Packet) -> Cmp:
    if type(left) is int and type(right) is int:
        return compare_ints(left, right)

    left_packet = left if type(left) is list else [left]
    right_packet = right if type(right) is list else [right]

    return compare_packets(left_packet, right_packet)


def compare_ints(left: int, right: int) -> Cmp:
    if left < right:
        return Cmp.LeftLower
    if right < left:
        return Cmp.RightLower
    return Cmp.Equal


def compare_packets(left: Packet, right: Packet) -> Cmp:
    num_pairs = min(len(left), len(right))
    for i in range(num_pairs):
        result = compare_either(left[i], right[i])
        if result != Cmp.Equal:
            return result
    if len(left) > num_pairs:
        return Cmp.RightLower
    if len(right) > num_pairs:
        return Cmp.LeftLower
    return Cmp.Equal


def main():
    packet_pairs: list[tuple[Packet, Packet]] = []
    with open("inputs/day_13.txt") as f:
        current_pair: list[Packet] = []
        for line in f.readlines():
            if line.isspace():
                continue
            current_pair.append(eval(line.strip()))

            if len(current_pair) == 2:
                packet_pairs.append((current_pair[0], current_pair[1]))
                current_pair = []

    good_indices = []
    for i, (left, right) in enumerate(packet_pairs):
        if compare_packets(left, right) == Cmp.LeftLower:
            good_indices.append(i + 1)

    print("Part 1:", sum(good_indices))

    packets = [[[2]], [[6]]]
    for pair in packet_pairs:
        packets += pair
    packets.sort(key=cmp_to_key(lambda x, y: compare_packets(x, y).value))
    two_index = packets.index([[2]]) + 1
    six_index = packets.index([[6]]) + 1
    print("Part 2:", two_index * six_index)


if __name__ == '__main__':
    main()
