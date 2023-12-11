import os


def read_file(file_name: str, strip_space: bool = True) -> list[str]:
    with open(file_name, "r") as file:
        return [line.strip() if strip_space else line.strip("\n") for line in file]


def are_ranges_intersecting(base: tuple[int, int], target: tuple[int, int]) -> bool:
    return base[0] <= target[1] and base[1] >= target[0]
