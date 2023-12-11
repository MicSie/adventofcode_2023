import basics
import os


class Mapping:
    def __init__(self, lines: list[str]) -> None:
        self.seed_input = read_seeds(lines[0])
        lines = lines[2:]
        (self.seed_to_soil_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.soil_to_fertilizer_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.fertilizer_to_water_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.water_to_light_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.light_to_temperature_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.temperature_to_humidity_map, read) = read_mapping(lines)
        lines = lines[read:]
        (self.humidity_to_location_map, _) = read_mapping(lines)

    def get_location_from_seed(self, seed: int) -> int:
        soil = read_from_mapping(self.seed_to_soil_map, seed)
        fertilizer = read_from_mapping(self.soil_to_fertilizer_map, soil)
        water = read_from_mapping(self.fertilizer_to_water_map, fertilizer)
        light = read_from_mapping(self.water_to_light_map, water)
        temperature = read_from_mapping(self.light_to_temperature_map, light)
        humidity = read_from_mapping(self.temperature_to_humidity_map, temperature)
        return read_from_mapping(self.humidity_to_location_map, humidity)

    def get_location_ranges_from_seedrange(self, seeds: range) -> set[range]:
        soil = read_from_mapping_ranges(self.seed_to_soil_map, {seeds})
        fertilizer = read_from_mapping_ranges(self.soil_to_fertilizer_map, soil)
        water = read_from_mapping_ranges(self.fertilizer_to_water_map, fertilizer)
        light = read_from_mapping_ranges(self.water_to_light_map, water)
        temperature = read_from_mapping_ranges(self.light_to_temperature_map, light)
        humidity = read_from_mapping_ranges(
            self.temperature_to_humidity_map, temperature
        )
        return read_from_mapping_ranges(self.humidity_to_location_map, humidity)

    def get_lowest_location_simple(self) -> int:
        seed_ranges = [range(seed, seed) for seed in self.seed_input]
        return self._find_lowest_in_range(seed_ranges)

    def get_lowest_location_range(self) -> int:
        seed_ranges = [
            range(
                self.seed_input[index],
                self.seed_input[index] + self.seed_input[index + 1],
            )
            for index in range(0, len(self.seed_input), 2)
        ]

        return self._find_lowest_in_range(seed_ranges)

    def _find_lowest_in_range(self, seed_ranges: list[range]) -> int:
        lowest = float("inf")
        for seed_range in seed_ranges:
            location_ranges = self.get_location_ranges_from_seedrange(seed_range)
            starts = [location_range.start for location_range in location_ranges]
            result = min(starts)
            lowest = min(result, lowest)

        return lowest


def read_seeds(line: str) -> list[int]:
    return [int(seed) for seed in line[len("seeds:") :].split()]


def read_mapping(lines: list[str]) -> tuple[set[tuple[range, range]], int]:
    result = set()
    read = 0
    start_found = False
    for line in lines:
        read += 1
        if "map:" in line:
            start_found = True
            continue
        if len(line) == 0:
            if start_found:
                break
            continue
        numbers = line.split()
        destination = int(numbers[0])
        source = int(numbers[1])
        count = int(numbers[2])
        result.add(
            (
                range(source, source + count),
                range(destination, destination + count),
            )
        )
    return (set(result), read)


def read_from_mapping(mapping: set[tuple[range, range]], seed: int) -> int:
    for map in mapping:
        source, _ = map
        if seed >= source.start and seed < source.stop:
            return map_seed(map, seed)
    return seed


def map_seed(map: tuple[range, range], seed: int) -> int:
    return map[1].start + (seed - map[0].start)


def read_from_mapping_ranges(
    mapping: set[tuple[range, range]], seed_ranges: set[range]
) -> set[range]:
    mapped = set()
    [
        mapped.update(read_from_mapping_range(mapping, seed_range))
        for seed_range in seed_ranges
    ]
    return compress_ranges(set(mapped))


def read_from_mapping_range(
    mapping: set[tuple[range, range]], seed_range: range
) -> set[range]:
    ranges_todo = {seed_range}
    found_ranges = set()
    while len(ranges_todo) > 0:
        found = False
        current_range = ranges_todo.pop()
        for map in mapping:
            source, _ = map
            if not basics.are_ranges_intersecting(
                (source.start, max(source.stop - 1, source.start)),
                (current_range.start, max(current_range.stop - 1, current_range.start)),
            ):
                continue

            found = True
            if current_range.start < source.start:
                ranges_todo.add(range(current_range.start, source.start))
                current_range = range(source.start, current_range.stop)

            if current_range.stop > source.stop:
                ranges_todo.add(range(source.stop, current_range.stop))
                current_range = range(current_range.start, source.stop)

            found_ranges.add(
                range(
                    map_seed(map, current_range.start),
                    map_seed(map, current_range.stop),
                )
            )

        if not found:
            found_ranges.add(current_range)

    return compress_ranges(found_ranges)


def compress_ranges(ranges: set[range]) -> set[range]:
    if len(ranges) <= 1:
        return ranges

    input = ranges.copy()
    output = set()
    while len(input) > 0:
        current_range = input.pop()
        restart = False
        for test_range in input:
            if not basics.are_ranges_intersecting(
                (current_range.start, current_range.stop),
                (test_range.start, test_range.stop),
            ):
                continue
            input.discard(test_range)
            input.add(
                range(
                    min(current_range.start, test_range.start),
                    max(current_range.stop, test_range.stop),
                )
            )
            restart = True
            break
        if not restart:
            output.add(current_range)
    return output


def run_day():
    print("Day05")
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    mapping = Mapping(lines)
    print(f"\tPart1: {mapping.get_lowest_location_simple()}")
    print(f"\tPart2: {mapping.get_lowest_location_range()}")


if __name__ == "__main__":
    run_day()
