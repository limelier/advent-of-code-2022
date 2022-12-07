from abc import abstractmethod, ABC
from typing import Iterable, Optional


class DirEntry(ABC):
    def __init__(self, name: str):
        self.name = name
        self.parent: Optional[Dir] = None

    @abstractmethod
    def get_size(self) -> int:
        pass


class File(DirEntry):
    def __init__(self, size: int, name: str):
        super().__init__(name)
        self.size = size

    def get_size(self) -> int:
        return self.size

    def __str__(self) -> str:
        return f"file {self.name} ({self.size})"


class Dir(DirEntry):

    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[DirEntry] = []

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)

    def walk(self) -> Iterable[DirEntry]:
        yield self
        for child in self.children:
            if isinstance(child, File):
                yield child
            elif isinstance(child, Dir):
                yield from child.walk()

    def __str__(self) -> str:
        return f"dir {self.name} ({len(self.children)} children, size {self.get_size()})"


def main():
    root = Dir("/")

    working_dir = None
    with open("inputs/day_07/day_07.txt", "r") as f:
        for line in f.readlines():
            match line.strip().split():
                case ["$", "cd", "/"]:
                    working_dir = root
                case ["$", "cd", ".."]:
                    working_dir = working_dir.parent
                case ["$", "cd", directory]:
                    working_dir = [child for child in working_dir.children if child.name == directory][0]
                case ["$", "ls"]:
                    pass
                case ["dir", dir_name]:
                    new_dir = Dir(dir_name)
                    new_dir.parent = working_dir
                    working_dir.children.append(new_dir)
                case [file_size, file_name]:
                    new_file = File(int(file_size), file_name)
                    new_file.parent = working_dir
                    working_dir.children.append(new_file)
                case _:
                    print("i am confused")

    sum_1 = sum(entry.get_size() for entry in root.walk() if isinstance(entry, Dir) and entry.get_size() <= 100000)
    print("Part 1:", sum_1)

    print("Part 2:")
    total = 70_000_000
    needed = 30_000_000
    unused = total - root.get_size()
    print(f"- unused space: {unused} (of {needed} needed)")
    delta = needed - unused
    print(f"- need to free {delta} more")
    candidates = (entry for entry in root.walk() if isinstance(entry, Dir) and entry.get_size() >= delta)
    target = min(candidates, key=lambda d: d.get_size())
    print(f"- smallest single directory you can delete for this is {target}")


if __name__ == '__main__':
    main()
