import basics
import os

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
NORTH_EAST = (1, -1)
NORTH_WEST = (-1, -1)
SOUTH_EAST = (1, 1)
SOUTH_WEST = (-1, 1)

ALL_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

FROM_NORTH = ["|", "7", "F"]
FROM_SOUTH = ["|", "L", "J"]
FROM_WEST = ["-", "L", "F"]
FROM_EAST = ["-", "7", "J"]


class Cell:
    def __init__(self, x: int, y: int, tile: chr) -> None:
        self.x = x
        self.y = y
        self.is_start = tile == "S"
        self.tile = tile
        self.is_visited = self.is_start
        self.is_current = False
        self.is_path = False
        self.coming_from = None
        self.sides = dict()
        self.set_sides(0, 0)
        self.side = 0

    def __eq__(self, other) -> bool:
        if isinstance(other, Cell):
            return self.x == other.x and self.y == other.y
        return False

    def define_sides(self) -> None:
        self.set_sides(1, 2)

    def set_sides(self, value1: int, value2: int) -> None:
        match self.tile:
            case "|":
                self.sides.update({NORTH_WEST: value1})
                self.sides.update({WEST: value1})
                self.sides.update({SOUTH_WEST: value1})

                self.sides.update({NORTH_EAST: value2})
                self.sides.update({EAST: value2})
                self.sides.update({SOUTH_EAST: value2})
            case "-":
                self.sides.update({NORTH_EAST: value1})
                self.sides.update({NORTH: value1})
                self.sides.update({NORTH_WEST: value1})

                self.sides.update({SOUTH_EAST: value2})
                self.sides.update({SOUTH: value2})
                self.sides.update({SOUTH_WEST: value2})
            case "L":
                self.sides.update({NORTH_EAST: value1})

                self.sides.update({NORTH_WEST: value2})
                self.sides.update({WEST: value2})
                self.sides.update({SOUTH_WEST: value2})
                self.sides.update({SOUTH: value2})
                self.sides.update({SOUTH_EAST: value2})
            case "J":
                self.sides.update({NORTH_WEST: value1})

                self.sides.update({NORTH_EAST: value2})
                self.sides.update({EAST: value2})
                self.sides.update({SOUTH_EAST: value2})
                self.sides.update({SOUTH: value2})
                self.sides.update({SOUTH_WEST: value2})
            case "7":
                self.sides.update({SOUTH_WEST: value1})

                self.sides.update({NORTH_WEST: value2})
                self.sides.update({NORTH: value2})
                self.sides.update({NORTH_EAST: value2})
                self.sides.update({EAST: value2})
                self.sides.update({SOUTH_EAST: value2})
            case "F":
                self.sides.update({SOUTH_EAST: value1})

                self.sides.update({NORTH_WEST: value2})
                self.sides.update({NORTH: value2})
                self.sides.update({NORTH_EAST: value2})
                self.sides.update({WEST: value2})
                self.sides.update({SOUTH_WEST: value2})

    def get_directions(self) -> list[tuple[int, int]]:
        match self.tile:
            case "|":
                directions = [NORTH, SOUTH]
            case "-":
                directions = [EAST, WEST]
            case "L":
                directions = [NORTH, EAST]
            case "J":
                directions = [NORTH, WEST]
            case "7":
                directions = [SOUTH, WEST]
            case "F":
                directions = [SOUTH, EAST]
            case "S":
                directions = ALL_DIRECTIONS
            case _:
                directions = list()
        return directions

    def update_sides(self) -> None:
        if self.coming_from == None or self.coming_from.is_start:
            return

        value1 = 0
        value2 = 0
        match self.tile:
            case "S":
                return
            case "|":
                match self.coming_from.tile:
                    case tile if tile in FROM_NORTH:
                        value2 = self.coming_from.sides[SOUTH_EAST]
                        value1 = self.coming_from.sides[SOUTH_WEST]
                    case tile if tile in FROM_SOUTH:
                        value2 = self.coming_from.sides[NORTH_EAST]
                        value1 = self.coming_from.sides[NORTH_WEST]

            case "-":
                match self.coming_from.tile:
                    case tile if tile in FROM_EAST:
                        value1 = self.coming_from.sides[NORTH_WEST]
                        value2 = self.coming_from.sides[SOUTH_WEST]
                    case tile if tile in FROM_WEST:
                        value1 = self.coming_from.sides[NORTH_EAST]
                        value2 = self.coming_from.sides[SOUTH_EAST]
            case "L":
                match self.coming_from.tile:
                    case tile if tile in FROM_NORTH:
                        value1 = self.coming_from.sides[SOUTH_EAST]
                    case tile if tile in FROM_EAST:
                        value1 = self.coming_from.sides[NORTH_WEST]

                value2 = self.coming_from.sides[SOUTH_WEST]
            case "J":
                match self.coming_from.tile:
                    case tile if tile in FROM_NORTH:
                        value1 = self.coming_from.sides[SOUTH_WEST]
                    case tile if tile in FROM_WEST:
                        value1 = self.coming_from.sides[NORTH_EAST]

                value2 = self.coming_from.sides[SOUTH_EAST]

            case "7":
                match self.coming_from.tile:
                    case tile if tile in FROM_SOUTH:
                        value1 = self.coming_from.sides[NORTH_WEST]
                    case tile if tile in FROM_WEST:
                        value1 = self.coming_from.sides[SOUTH_EAST]

                value2 = self.coming_from.sides[NORTH_EAST]

            case "F":
                match self.coming_from.tile:
                    case tile if tile in FROM_SOUTH:
                        value1 = self.coming_from.sides[NORTH_EAST]
                    case tile if tile in FROM_EAST:
                        value1 = self.coming_from.sides[SOUTH_WEST]

                value2 = self.coming_from.sides[NORTH_WEST]

        self.set_sides(value1, value2)


class MazeHolder:
    def __init__(self, file_name) -> None:
        self.done = False
        self.grid = list()
        for row, input_line in enumerate(basics.read_file(file_name)):
            row_list = list()
            for column, cell_input in enumerate(input_line):
                cell = Cell(column, row, cell_input)
                if cell.is_start:
                    self.current_cell = self.start = cell
                row_list.append(cell)
            self.grid.append(row_list)
        self.path = list()

    def get_steps_to_farthest_point(self) -> int:
        while not self.done:
            self.run_cycle()
        return len(self.path) / 2

    def count_inside_cells(self) -> int:
        if not self.done:
            self.get_steps_to_farthest_point()

        outside = 0
        side = 0
        empty_cells = list
        counter = 0
        for row in self.grid:
            empty_cells = list()
            side = outside
            for column in row:
                if column.is_start:
                    continue
                elif column.is_path:
                    if NORTH_WEST in column.sides:
                        side = column.sides[NORTH_WEST]
                        if outside == 0:
                            outside = side

                    if len(empty_cells):
                        for empty_cell in empty_cells:
                            empty_cell.side = side
                        empty_cells = list()

                    if NORTH_EAST in column.sides:
                        side = column.sides[NORTH_EAST]
                else:
                    if side == 0:
                        empty_cells.append(column)
                    else:
                        column.side = side
                        counter += 0 if side == outside else 1

        return counter

    def run_cycle(
        self,
    ) -> None:
        if len(self.path) > 1 and self.current_cell.is_start:
            self.has_found_path = True
            self.done = True
            for node in self.path:
                node.is_path = True
            return

        self._update_current_cell()

    def _get_all_neighbors(self, cell: Cell) -> list[Cell]:
        neighbors = []

        for direction_x, direction_y in ALL_DIRECTIONS:
            x = cell.x + direction_x
            y = cell.y + direction_y
            if y < 0 or x < 0 or x >= (len(self.grid[0])) or y >= (len(self.grid)):
                continue
            neighbors.append(self.grid[y][x])
        return neighbors

    def _update_current_cell(self):
        if self.current_cell == None:
            self.current_cell = self.start
        elif all([side == 0 for side in self.current_cell.sides.values()]):
            self.current_cell.define_sides()

        self.current_cell.is_current = False
        self.current_cell.is_visited = True
        self.path.append(self.current_cell)

        for neighbor in self._get_neighbors(self.current_cell):
            if (
                neighbor == self.current_cell.coming_from
                or neighbor == self.current_cell
                or neighbor.is_visited
            ):
                continue
            neighbor.coming_from = self.current_cell
            neighbor.update_sides()
            self.current_cell = neighbor
            neighbor.is_current = True
            return

        self.start.coming_from = self.current_cell
        self.current_cell = self.start

    def _get_neighbors(self, cell: Cell) -> list[Cell]:
        neighbors = list()

        for direction_x, direction_y in cell.get_directions():
            x = cell.x + direction_x
            y = cell.y + direction_y
            if y < 0 or x < 0 or x >= (len(self.grid[0])) or y >= (len(self.grid)):
                continue
            neighbor = self.grid[y][x]
            neighbor_directions = neighbor.get_directions()

            if (direction_x, direction_y) == NORTH and not SOUTH in neighbor_directions:
                continue
            if (direction_x, direction_y) == SOUTH and not NORTH in neighbor_directions:
                continue
            if (direction_x, direction_y) == EAST and not WEST in neighbor_directions:
                continue
            if (direction_x, direction_y) == WEST and not EAST in neighbor_directions:
                continue

            neighbors.append(neighbor)
        return neighbors


def run_day():
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
    maze = MazeHolder(file)
    print("Day10")
    print(f"\tPart1: {maze.get_steps_to_farthest_point()}")
    print(f"\tPart2: {maze.count_inside_cells()}")


if __name__ == "__main__":
    run_day()
