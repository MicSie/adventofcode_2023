import functools
import multiprocessing
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

    @functools.cache
    def get_location_from_seed(self, seed: int) -> int:
        soil = read_from_mapping(self.seed_to_soil_map, seed)
        return self.get_location_from_soil(soil)

    @functools.cache
    def get_location_from_soil(self, soil: int) -> int:
        fertilizer = read_from_mapping(self.soil_to_fertilizer_map, soil)
        return self.get_location_from_fertilizer(fertilizer)

    @functools.cache
    def get_location_from_fertilizer(self, fertilizer: int) -> int:
        water = read_from_mapping(self.fertilizer_to_water_map, fertilizer)
        return self.get_location_from_water(water)

    @functools.cache
    def get_location_from_water(self, water: int) -> int:
        light = read_from_mapping(self.water_to_light_map, water)
        return self.get_location_from_light(light)

    @functools.cache
    def get_location_from_light(self, light: int) -> int:
        temperature = read_from_mapping(self.light_to_temperature_map, light)
        return self.get_location_from_temperature(temperature)

    @functools.cache
    def get_location_from_temperature(self, temperature: int) -> int:
        humidity = read_from_mapping(self.temperature_to_humidity_map, temperature)
        return self.get_location_from_humidity(humidity)

    @functools.cache
    def get_location_from_humidity(self, humidity: int) -> int:
        return read_from_mapping(self.humidity_to_location_map, humidity)

    def get_lowest_location_simple(self) -> int:
        seeds = {seed: self.get_location_from_seed(seed) for seed in self.seed_input}
        return sorted(seeds.values())[0]

    def get_lowest_location_range(self) -> int:
        seed_ranges = [
            range(
                self.seed_input[index],
                self.seed_input[index] + self.seed_input[index + 1],
            )
            for index in range(0, len(self.seed_input), 2)
        ]

        seeds = list()
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            for result in pool.map(self._find_lowest_in_range, seed_ranges):
                if result != None:
                    seeds.append(result)

        return sorted(seeds)[0]

    def _find_lowest_in_range(self, seed_range: range) -> int:
        lowest = None
        for seed_id in seed_range:
            location = self.get_location_from_seed(seed_id)
            if lowest == None or lowest > location:
                lowest = location
        return lowest


def read_seeds(line: str) -> list[int]:
    return [int(seed) for seed in line[len("seeds:") :].split()]


def read_mapping(lines: list[str]) -> tuple[frozenset[tuple[int, int, int]], int]:
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
        result.add((source, destination, count))
    return (frozenset(result), read)


# frozenset to make it hashable
# @functools.cache
def read_from_mapping(mapping: frozenset[tuple[int, int, int]], key: int) -> int:
    for source, destination, count in mapping:
        if key >= source and key <= source + count:
            return destination + (key - source)
    return key


def run_day():
    print("Day05")
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    lines = basics.read_file(file)
    mapping = Mapping(lines)
    print(f"\tPart1: {mapping.get_lowest_location_simple()}")
    print(f"\tPart2: {mapping.get_lowest_location_range()}")


if __name__ == "__main__":
    run_day()
