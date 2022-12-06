from collections import deque

queue = deque()


def insert_into_queue(new: str, target: int) -> bool:
    """
    Add ``new`` element to queue, pop oldest if over ``target`` length, and return ``True`` if queue is ``target``
    distinct items
    """
    should_check_all = True
    # simple preliminary check; avoid complicated check until this passes
    if new in queue:
        should_check_all = False

    queue.append(new)
    if len(queue) > target:
        queue.popleft()

    return len(queue) == target \
        and should_check_all \
        and len(set(queue)) == target


def main():
    done_4 = False

    with open("inputs/day_06.txt", "r") as f:
        i = 0
        while True:
            i += 1

            char = f.read(1)
            if not char:  # EOF
                break

            if not done_4:
                if insert_into_queue(char, 4):
                    print(f"Part 1: {i} - {''.join(queue)}")
                    done_4 = True
            elif insert_into_queue(char, 14):
                print(f"Part 2: {i} - {''.join(queue)}")
                break


if __name__ == '__main__':
    main()
