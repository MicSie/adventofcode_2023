import itertools
import multiprocessing
import time
import basics
import os
import re


REPLACEMENTS = ["#", "."]


def get_arrangement_count(line: str, multiplier: int = 1) -> int:
    pattern, numbers = line.split()
    numbers = [number.strip() for number in numbers.split(",")]
    return count_arrangements(pattern, numbers, multiplier)


def sum_arrangements(lines: list[str], multiplier: int = 1) -> int:
    counts = list()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        data = zip(lines, itertools.repeat(multiplier))
        for count_result in pool.starmap(get_arrangement_count, data):
            if count_result != None:
                counts.append(count_result)

    return sum(counts)


def count_arrangements(pattern: str, numbers: list[str], multiplier: int = 1) -> int:
    result = _build_arrangements("?".join([pattern] * multiplier), numbers * multiplier)
    return sum(1 for _ in result)


def _get_regex_for_number(number: str) -> str:
    if number == "1":
        return r"(?:#|\?)"
    else:
        return "(?:" + "".join([r"(?:#|\?)"] * int(number)) + ")"


def _build_arrangements(pattern: str, numbers: list[str]) -> list[str]:
    number_regex = re.compile(
        r"^(?:\.|\?)*"
        + r"(?:\.|\?)+".join([_get_regex_for_number(number) for number in numbers])
        + r"(?:\.|\?)*$"
    )

    result = {pattern}
    for _ in range(pattern.count("?")):
        result = _check_pattern(number_regex, result)
    return result


def _check_pattern(number_regex: re.Pattern[str], enries: list[str]) -> list[str]:
    for current_pattern in enries:
        for replacement in REPLACEMENTS:
            new_value = current_pattern.replace("?", replacement, 1)
            if number_regex.match(new_value):
                yield new_value


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    print("Day12")
    start = time.time()
    count = sum_arrangements(lines)
    end = time.time()
    print(f"\tPart1: {count} ({end-start})")
    start = time.time()
    count = sum_arrangements(lines, 5)
    end = time.time()
    print(f"\tPart2: {count} ({end-start})")


if __name__ == "__main__":
    run_day()
