import basics
import os


def is_adjacent_to_symbol(input: list, row: int, column: int, length: int) -> bool:
    for r in range(row - 1, row + 2):
        if r < 0 or r >= len(input):
            continue

        start = max(0, column - 1)
        end = min(len(input[r]), column + length + 1)
        for char in input[r][start:end]:
            if not char.isdigit() and char != ".":
                return True

    return False


def get_numbers(input: list, row: int, column: int) -> tuple:
    number1 = -1
    for r in range(row - 1, row + 2):
        if r < 0 or r >= len(input):
            continue

        start = max(0, column - 1)
        end = min(len(input[r]), column + 2)
        skip_to_position = -1
        for position, char in enumerate(input[r][start:end]):
            if not char.isdigit() or skip_to_position > position:
                continue

            position += start
            while position > 0:
                if input[r][position].isdigit():
                    position -= 1
                else:
                    break

            number = ""
            while position < len(input[r]):
                if input[r][position].isdigit():
                    number += input[r][position]
                elif number != "":
                    break
                position += 1
            if number != "":
                if number1 < 0:
                    number1 = int(number)
                    skip_to_position = position - start
                else:
                    return (number1, int(number))

    return (0, 0)


def get_sum_of_parts(fileName: str) -> int:
    current_row = 0
    result = 0
    lines = basics.read_file(fileName)
    for line in lines:
        current_column = 0
        length = 0
        number = ""
        while current_column < len(line):
            while current_column < len(line) and line[current_column].isdigit():
                number += line[current_column]
                length += 1
                current_column += 1

            if number != "" and is_adjacent_to_symbol(
                lines, current_row, current_column - length, length
            ):
                result += int(number)

            length = 0
            number = ""

            current_column += 1

        current_row += 1

    return result


def get_gear_ratio(fileName: str) -> int:
    current_row = 0
    result = 0
    lines = basics.read_file(fileName)
    for line in lines:
        current_column = 0
        length = 0
        number = ""
        while current_column < len(line):
            if line[current_column] == "*":
                numbers = get_numbers(lines, current_row, current_column)
                result += numbers[0] * numbers[1]

            current_column += 1

        current_row += 1

    return result


def run_day():
    basics.ensure_directory(os.path.dirname(__file__))
    print("Day03")
    print(f"\tPart1: {get_sum_of_parts('input.txt')}")
    print(f"\tPart2: {get_gear_ratio('input.txt')}")


if __name__ == "__main__":
    run_day()
