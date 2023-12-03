import basics
import re
import os

game_id_regex = re.compile(r"(?<=ame )\d+")
blue_regex = re.compile(r"\d+(?= blue)")
green_regex = re.compile(r"\d+(?= green)")
red_regex = re.compile(r"\d+(?= red)")


def read_line(line: str) -> tuple:
    id = int(game_id_regex.findall(line)[0])
    blue = max([int(blue) for blue in blue_regex.findall(line)])
    green = max([int(green) for green in green_regex.findall(line)])
    red = max([int(red) for red in red_regex.findall(line)])

    return (id, blue, green, red)


def get_possible_sum(fileName: str, game_parameters: tuple) -> int:
    sum = 0
    lines = basics.read_file(fileName)
    for line in lines:
        parsed = read_line(line)
        if (
            game_parameters[0] >= parsed[1]
            and game_parameters[1] >= parsed[2]
            and game_parameters[2] >= parsed[3]
        ):
            sum += parsed[0]

    return sum


def get_power(fileName: str) -> int:
    return sum(
        [
            parsed[1] * parsed[2] * parsed[3]
            for parsed in [read_line(line) for line in basics.read_file(fileName)]
        ]
    )


def run_day():
    basics.ensure_directory(os.path.dirname(__file__))
    print("Day02")
    print(f"\tPart1: {get_possible_sum('input', (14, 13, 12))}")
    print(f"\tPart2: {get_power('input')}")


if __name__ == "__main__":
    run_day()
