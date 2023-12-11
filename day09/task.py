import basics
import os


def parse(lines: list[str]) -> list[int]:
    return [[int(item) for item in line.split()] for line in lines]


def get_differences(line: list[int]) -> list[int]:
    return [line[index + 1] - item for index, item in enumerate(line[:-1])]


def predict(line: list[int], future: bool) -> int:
    differences = get_differences(line)
    if not all([difference == 0 for difference in differences]):
        prediction = predict(differences, future)
    elif future:
        prediction = differences[-1]
    else:
        prediction = differences[0]

    if future:
        return line[-1] + prediction
    return line[0] - prediction


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    print("Day09")
    print(f"\tPart1: {sum([predict(line, True) for line in parse(lines)])}")
    print(f"\tPart2: {sum([predict(line, False) for line in parse(lines)])}")


if __name__ == "__main__":
    run_day()
