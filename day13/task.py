import itertools
import basics
import os


def sum_mirror_lines_with_error(data: list[list[str]], error: int = 1) -> int:
    result = 0
    for pattern in data:
        line = find_mirror_line_with_error(rotated, error)
        if line != None:
            result += line
            continue

        rotated = rotate(pattern)
        line = find_mirror_line_with_error(pattern, error)
        if line != None:
            result += line * 100

    return result


def sum_mirror_lines(data: list[list[str]]) -> int:
    result = 0
    for pattern in data:
        lines = find_matching_lines(pattern)
        line = find_mirror_line(lines)
        if line != None:
            result += (line + 1) * 100
            continue

        rotated = rotate(pattern)
        lines = find_matching_lines(rotated)
        line = find_mirror_line(lines)
        if line != None:
            result += line + 1

    return result


def rotate(data: list[list[str]]) -> list[list[str]]:
    return list(["".join(line) for line in zip(*data[::-1])])


def find_matching_lines(lines: list[str]) -> dict[str, list[int, int]]:
    result = dict()
    for index, line in enumerate(lines):
        if line in result:
            result[line].append(index)
        else:
            result[line] = [index]
    return result


def find_mirror_line_with_error(pattern: list[str], error: int = 1) -> int:
    for index in range(1, len(pattern)):
        top = pattern[:index][::-1]
        bottom = pattern[index:]
        if _count_string_diff(top[0], bottom[0]) > error:
            continue

        smallest = min(len(top), len(bottom))
        top = top[:smallest]
        bottom = bottom[:smallest]
        if (
            sum(
                [
                    _count_string_diff(line, bottom[test_index])
                    for test_index, line in enumerate(top)
                ]
            )
            == error
        ):
            return index
    return None


def _count_string_diff(string1: str, string2: str) -> int:
    return sum([int(char != string2[index]) for index, char in enumerate(string1)])


def find_mirror_line(data: dict[str, list[int, int]]) -> int:
    if all([len(value) == 1 for value in data.values()]):
        return None
    data_values = list()
    for data_value in data.values():
        if len(data_value) == 1:
            data_values.append((data_value[0], data_value[0]))
            continue
        if len(data_value) == 2:
            data_values.append(tuple(data_value))
            continue
        data_values.extend(itertools.combinations(data_value, 2))

    def is_mirror(current: tuple[int, int]) -> bool:
        if current == None:
            return False
        max_val = max([value for enries in data_values for value in enries])
        for index in range(current[0], -1, -1):
            delta = current[0] - index
            if (index, current[1] + delta) in data_values:
                if index == 0 or current[1] + delta == max_val:
                    return True
            else:
                return False
        return False

    for entry in data_values:
        if abs(entry[0] - entry[1]) == 1 and is_mirror(entry):
            return entry[0]

    return None


def parse(lines: list[str]) -> list[list[str]]:
    result = list()
    current = list()
    for line in lines:
        if len(line) == 0:
            result.append(current)
            current = list()
        else:
            current.append(line)
    if len(current) > 0:
        result.append(current)
    return result


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    parsed = parse(lines)
    print("Day13")
    print(f"\tPart1: {sum_mirror_lines(parsed)}")
    print(f"\tPart2: {sum_mirror_lines_with_error(parsed)}")


if __name__ == "__main__":
    run_day()
