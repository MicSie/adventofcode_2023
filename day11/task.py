import basics
import os


def expand(lines: list[str]) -> list[str]:
    empty_columns = list()
    for index, _ in enumerate(lines[0]):
        all_empty = True
        for line in lines:
            if line[index] == "#":
                all_empty = False
                break
        if all_empty:
            empty_columns.append(index)

    result = list()
    empty_line = "." * (len(lines[0]) + len(empty_columns))
    for line in lines:
        offset = 0
        result_line = line
        for index in empty_columns:
            index += offset
            result_line = result_line[:index] + "." + result_line[index:]
            offset += 1
        result.append(result_line)
        if result_line == empty_line:
            result.append(empty_line)

    return result


def expands(lines: list[str]) -> tuple[list[int], list[int]]:
    empty_columns = list()
    empty_lines = set()
    empty_line = "." * len(lines[0])
    for column_index, _ in enumerate(lines[0]):
        all_empty = True
        for line_index, line in enumerate(lines):
            if line[column_index] == "#":
                all_empty = False
                break
            if len(empty_columns) == 0 and line == empty_line:
                empty_lines.add(line_index)

        if all_empty:
            empty_columns.append(column_index)

    return (empty_columns, list(empty_lines))


def find_galaxies(lines: list[str]) -> list[tuple[int, int]]:
    result = list()
    for line_index, line in enumerate(lines):
        for column_index, column in enumerate(line):
            if column == "#":
                result.append((column_index, line_index))
    return result


def sum_shortes_routes(lines: list[str], expansion: int) -> int:
    galaxies = find_galaxies(lines)
    expansions = expands(lines)
    result = 0
    galaxies = galaxies.copy()
    expansion = expansion - 1  # the original line
    while len(galaxies) > 1:
        current_galaxy = galaxies.pop()
        for galaxy in galaxies:
            result += get_range(current_galaxy, galaxy, expansions, expansion)

    return result


def get_range(
    galaxy1: tuple[int, int],
    galaxy2: tuple[int, int],
    expansions: tuple[list[int], list[int]] = (list(), list()),
    expansion: int = 0,
) -> int:
    galaxy1_column, galaxy1_line = galaxy1
    galaxy2_column, galaxy2_line = galaxy2
    galaxy1_column_multiplier = galaxy2_column_multiplier = 0
    galaxy1_line_multiplier = galaxy2_line_multiplier = 0
    empty_columns, empty_lines = expansions
    for empty_column in empty_columns:
        if galaxy1_column > empty_column:
            galaxy1_column_multiplier += 1
        if galaxy2_column > empty_column:
            galaxy2_column_multiplier += 1
    for empty_line in empty_lines:
        if galaxy1_line > empty_line:
            galaxy1_line_multiplier += 1
        if galaxy2_line > empty_line:
            galaxy2_line_multiplier += 1

    return abs(
        (galaxy1_column + (expansion * galaxy1_column_multiplier))
        - (galaxy2_column + (expansion * galaxy2_column_multiplier))
    ) + abs(
        (galaxy1_line + (expansion * galaxy1_line_multiplier))
        - (galaxy2_line + (expansion * galaxy2_line_multiplier))
    )


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    print("Day11")
    print(f"\tPart1: {sum_shortes_routes(lines,2)}")
    print(f"\tPart2: {sum_shortes_routes(lines,1000000)}")


if __name__ == "__main__":
    run_day()
