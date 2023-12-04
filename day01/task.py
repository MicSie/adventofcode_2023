import basics
import os


def read_simple_calibration_sum_from_file(fileName: str) -> list:
    lines = basics.read_file(fileName)
    sum = 0
    for line in lines:
        numbers = [char for char in line if char.isdigit()]
        number = numbers[0] + numbers[-1]
        sum += int(number)
    return sum


def read_calibration_sum_from_file(fileName: str) -> list:
    lines = basics.read_file(fileName)
    sum = 0
    for line in lines:
        numbers = [char for char in replace_numbers(line) if char.isdigit()]
        number = numbers[0] + numbers[-1]
        sum += int(number)
    return sum


replacements = [
    ("zero"),
    ("one"),
    ("two"),
    ("three"),
    ("four"),
    ("five"),
    ("six"),
    ("seven"),
    ("eight"),
    ("nine"),
]


def replace_numbers(line: str):
    for num, name in enumerate(replacements):
        line = line.replace(name, f"{name}{num}{name}")
    return line


def run_day():
    basics.ensure_directory(os.path.dirname(__file__))
    print("Day01")
    print("\tPart1: " + str(read_simple_calibration_sum_from_file("input.txt")))
    print("\tPart2: " + str(read_calibration_sum_from_file("input.txt")))


if __name__ == "__main__":
    run_day()
