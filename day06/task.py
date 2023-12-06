from math import sqrt, pow, ceil
import basics
import os


def get_times_distances(lines: list[str]) -> list[tuple[int, int]]:
    times = [int(time) for time in lines[0][len("Time:") :].split()]
    distances = [int(distance) for distance in lines[1][len("Distance:") :].split()]
    return [(time, distances[index]) for index, time in enumerate(times)]


def get_time_distance(lines: list[str]) -> tuple[int, int]:
    time = lines[0][len("Time:") :].replace(" ", "")
    distance = lines[1][len("Distance:") :].replace(" ", "")
    return (int(time), int(distance))


def get_options_count(input: tuple[int, int]) -> int:
    # distance < speed * ( time - speed )
    # d < v * ( t - v )
    # 0 = vt - v² - d
    # 0 = v² - vt - d <= Quadratic equation!
    # 0 = ( -(-t) ) +- SQRT( (-t)² -4d ) / 2
    # 0 = ( t +- SQRT( t² -4d ) / 2

    time, distance = input
    zero_speed = (time - sqrt(pow(time, 2) - 4 * distance)) / 2
    speed = int(ceil(zero_speed))
    if zero_speed == speed:
        speed += 1

    return time - (2 * speed) + 1


def beat_record(input: list[tuple[int, int]]) -> int:
    record = 1
    for timings in input:
        record *= get_options_count(timings)
    return record


def run_day():
    basics.ensure_directory(os.path.dirname(__file__))
    lines = basics.read_file("input.txt")
    print("Day06")
    print(f"\tPart1: {beat_record(get_times_distances(lines))}")
    print(f"\tPart2: {get_options_count(get_time_distance(lines))}")


if __name__ == "__main__":
    run_day()
