import math
import basics
import os
from sys import setrecursionlimit


def parse(lines: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    instructions = lines[0]
    nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}
    return (instructions, nodes)


def count_all_steps(
    input_data: tuple[str, dict[str, tuple[str, str]]],
    start_suffix: str,
    target_suffix: str,
) -> int:
    instructions, nodes = input_data
    steps = [
        count_steps(instructions, nodes, node, target_suffix)
        for node in nodes
        if node.endswith(start_suffix)
    ]

    return math.lcm(*steps)


def count_steps(
    instructions: str,
    nodes: dict[str, tuple[str, str]],
    current_node: str,
    target_suffix: str,
) -> int:
    instruction_index = 0
    step = 0
    while not current_node.endswith(target_suffix):
        step += 1
        if instructions[instruction_index] == "L":
            index = 0
        else:
            index = 1
        current_node = nodes[current_node][index]
        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0
    return step


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    data = parse(basics.read_file(file))
    print("Day08")
    print(f"\tPart1: {count_steps(data[0],data[1], 'AAA', 'ZZZ')}")
    print(f"\tPart2: {count_all_steps(data, 'A', 'Z')}")


if __name__ == "__main__":
    run_day()
