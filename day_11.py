from dataclasses import dataclass
from typing import Callable
from itertools import groupby


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]  # old -> new
    test_divisor: int
    true_monkey_index: int
    false_monkey_index: int

    inspections: int = 0

    def __init__(self, input_lines: list[str]):
        self.items = [int(item.strip()) for item in input_lines[1].split(":")[1].split(",")]
        self.operation = lambda old: eval(input_lines[2].split("new = ")[1])
        self.test_divisor = int(input_lines[3].split("by ")[1])
        self.true_monkey_index = int(input_lines[4].split("monkey ")[1])
        self.false_monkey_index = int(input_lines[5].split("monkey ")[1])


def read_monkeys():
    input_lines = (line.strip() for line in open("inputs/day_11/day_11.txt").readlines())
    # input_lines = (line.strip() for line in open("inputs/day_11/example.txt").readlines())
    input_blocks = [
        list(group)
        for k, group in groupby(input_lines, lambda line: line == "")
        if not k
    ]
    return [Monkey(block) for block in input_blocks]


def print_monkeys(monkeys: list[Monkey]):
    for i, monkey in enumerate(monkeys):
        print(f"{i} - {monkey.items}, ins={monkey.inspections}")


def simulate_monkeys(monkeys: list[Monkey], rounds: int, do_division: bool) -> int:
    """
    Simulate the monkeys and return the level of monkey business.
    :param monkeys: the list of monkeys before the first round
    :param rounds: how many rounds to go for
    :param do_division: whether to // 3 worry levels after applying operations
    :return: the product of the # of inspections for the two most active monkeys
    """

    print_monkeys(monkeys)

    for rnd in range(1, rounds + 1):
        for monkey in monkeys:
            for item in monkey.items:
                new_worry = monkey.operation(item)
                if do_division:
                    new_worry //= 3
                target_idx = monkey.true_monkey_index \
                    if (new_worry % monkey.test_divisor == 0) \
                    else monkey.false_monkey_index
                monkeys[target_idx].items.append(new_worry)
            monkey.inspections += len(monkey.items)
            monkey.items = []
        print()
        print(f"Round {rnd}:")
        print_monkeys(monkeys)

    monkeys_by_inspections = sorted(monkeys, key=lambda m: m.inspections)
    return monkeys_by_inspections[-1].inspections * monkeys_by_inspections[-2].inspections


def main():
    monkeys = read_monkeys()

    # uncomment one (part 2 doesn't actually work lmao):
    result = simulate_monkeys(monkeys, 20, True)  # part 1
    # result = simulate_monkeys(monkeys, 10000, False)  # part 2

    print()
    print("Result:", result)


if __name__ == '__main__':
    main()
