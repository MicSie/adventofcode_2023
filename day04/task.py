import re
import basics
import os

card_id_regex = re.compile(r"(?<=ard)\s*\d+\s*(?=:)")
wining_regex = re.compile(r"(?<=:).*(?=\|)")
numbers_regex = re.compile(r"(?<=\|).*")


def parse_line(line: str) -> tuple:
    card_id = int(card_id_regex.findall(line)[0])
    wining_numbers = [int(number) for number in wining_regex.findall(line)[0].split()]
    numbers = [int(number) for number in numbers_regex.findall(line)[0].split()]
    return (card_id, wining_numbers, numbers)


def parse_lines(lines: list[str]) -> list[tuple]:
    return [parse_line(line) for line in lines]


def calculate_value(input: list[tuple]) -> int:
    result = 0

    for line in input:
        wining = set(line[1])
        numbers = set(line[2])
        wining_numbers = len(wining.intersection(numbers))
        if wining_numbers == 0:
            continue

        result += pow(2, wining_numbers - 1)

    return result


def count_cards(input: list[tuple]) -> int:
    histogram = {line[0]: 1 for line in input}

    for line in input:
        current_card = line[0]
        card_count = histogram[current_card]
        wining = set(line[1])
        numbers = set(line[2])
        wining_numbers = len(wining.intersection(numbers))
        if wining_numbers == 0:
            continue

        for card in range(current_card + 1, current_card + 1 + wining_numbers):
            histogram[card] += card_count

    return sum([histogram[card] for card in histogram])


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    parsed_lines = parse_lines(lines)
    print("Day04")
    print(f"\tPart1: {calculate_value(parsed_lines)}")
    print(f"\tPart2: {count_cards(parsed_lines)}")


if __name__ == "__main__":
    run_day()
