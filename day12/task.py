import itertools
import multiprocessing
import time
import basics
import os


REPLACEMENTS = ["#", "."]


def get_arrangement_count(line: str, multiplier: int = 1) -> int:
    pattern, numbers = line.split()
    numbers = [int(number) for number in numbers.split(",")]
    return count_arrangements(pattern, numbers, multiplier)


def sum_arrangements(lines: list[str], multiplier: int = 1) -> int:
    counts = list()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        data = zip(lines, itertools.repeat(multiplier))
        for count_result in pool.starmap(get_arrangement_count, data):
            if count_result != None:
                counts.append(count_result)

    return sum(counts)


def count_arrangements(pattern: str, numbers: list[int], multiplier: int = 1) -> int:
    pattern = "?".join([pattern] * multiplier)
    numbers *= multiplier

    cache = dict()

    def count_matches(pattern_index: int, number_index: int, current_block_size) -> int:
        key = (pattern_index, number_index, current_block_size)
        if key in cache:
            return cache[key]
        if pattern_index == len(pattern):
            return int(
                # no block, all numbers accounted for
                (number_index == len(numbers) and current_block_size == 0)
                or
                # or currend block is last number
                (number_index == len(numbers) - 1 and current_block_size == numbers[-1])
            )

        counter = 0
        if pattern[pattern_index] in ".?":  # is space
            if current_block_size == 0:
                counter += count_matches(pattern_index + 1, number_index, 0)
            else:
                if number_index == len(numbers):
                    return 0  # end of possible numbers
                if current_block_size == numbers[number_index]:  # next number
                    counter += count_matches(pattern_index + 1, number_index + 1, 0)
        if pattern[pattern_index] in "#?":  # is number
            counter += count_matches(
                pattern_index + 1, number_index, current_block_size + 1
            )
        cache[key] = counter
        return counter

    return count_matches(0, 0, 0)


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
