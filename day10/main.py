import os
import sys
import context
from datetime import datetime
import task
import pygame
from pygame.locals import *

VISUAL = True

SIDE1_COLOR = (0, 0, 100)
SIDE2_COLOR = (0, 100, 0)
HEIGHT = 1000
WIDTH = 1800
SHOW_GRID = False
# FILE_NAME = os.path.join(
#     os.path.abspath(os.path.dirname(__file__)), "../tests/inputs/day10_5.txt"
# )
FILE_NAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


class App:
    def __init__(self):
        self.maze_holder = task.MazeHolder(FILE_NAME)
        self.maze_holder.count_inside_cells()
        row_number = len(self.maze_holder.grid)
        column_number = len(self.maze_holder.grid[0])

        row_size = HEIGHT // row_number
        col_size = WIDTH // column_number

        self._cell_size = min(row_size, col_size)

        self.width = column_number * self._cell_size
        self.height = row_number * self._cell_size

        self._running = False
        self._display = None
        self._created_gif = False
        self.size = self.width, self.height
        self._update_clock_event = pygame.USEREVENT + 2

    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._update_clock()
        self._one_last_update = True
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == self._update_clock_event:
            self._update_clock()

    def on_loop(self):
        if not self.maze_holder.done:
            self.maze_holder.run_cycle()

    def on_render(self):
        if not self.maze_holder.done:
            self._draw_grid()
        elif self._one_last_update:
            self._draw_grid()
            self._one_last_update = False

    def _draw_grid(self):
        for row_list in self.maze_holder.grid:
            for cell in row_list:
                self._draw_cell(cell)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        pygame.time.set_timer(self._update_clock_event, 500)
        self._draw()
        clock = pygame.time.Clock()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            # clock.tick(60)
        self.on_cleanup()

    def _update_clock(self):
        pygame.display.set_caption(datetime.now().strftime("%X.%f"))

    def _draw(self):
        for row in self.maze_holder.grid:
            for cell in row:
                self._draw_cell(cell)

    def _draw_cell(self, cell: task.Cell):
        x_min = cell.x * self._cell_size
        x_center = x_min + (self._cell_size // 2)
        x_max = x_min + self._cell_size
        y_min = cell.y * self._cell_size
        y_center = y_min + (self._cell_size // 2)
        y_max = y_min + self._cell_size

        if SHOW_GRID:
            rect = pygame.Rect(x_min, y_min, self._cell_size, self._cell_size)
            pygame.draw.rect(self._display, (255, 255, 255), rect, 1)

        self.draw_sides(cell, x_min, y_min)

        if cell.is_start:
            color = (0, 255, 0)
            pygame.draw.circle(
                self._display, color, (x_center, y_center), self._cell_size // 2
            )
            return
        if cell.is_path:
            color = (0, 255, 255)
        elif cell.is_visited:
            color = (255, 255, 255)
        elif cell.is_current:
            color = (255, 0, 0)
        else:
            color = (150, 150, 150)

        match cell.tile:
            case "|":
                points = [(x_center, y_min), (x_center, y_max)]
            case "-":
                points = [(x_min, y_center), (x_max, y_center)]
            case "L":
                points = [(x_max, y_center), (x_center, y_center), (x_center, y_min)]
            case "J":
                points = [(x_min, y_center), (x_center, y_center), (x_center, y_min)]
            case "7":
                points = [(x_min, y_center), (x_center, y_center), (x_center, y_max)]
            case "F":
                points = [(x_max, y_center), (x_center, y_center), (x_center, y_max)]
            case _:
                return

        pygame.draw.lines(self._display, color, False, points, 1)

    def draw_sides(self, cell, x_min, y_min):
        if cell.is_start:
            return
        if not cell.is_path:
            if 1 == cell.side:
                color = SIDE1_COLOR
            elif 2 == cell.side:
                color = SIDE2_COLOR
            else:
                return
            rect = pygame.Rect(x_min, y_min, self._cell_size, self._cell_size)
            pygame.draw.rect(self._display, color, rect)

        size = self._cell_size // 3
        color = (0, 0, 0)
        for y_index, x in enumerate(range(-1, 2)):
            for x_index, y in enumerate(range(-1, 2)):
                side_coords = (y, x)
                if side_coords not in cell.sides:
                    continue
                else:
                    side = cell.sides[side_coords]
                if 1 == side:
                    color = SIDE1_COLOR
                elif 2 == side:
                    color = SIDE2_COLOR
                else:
                    continue
                rect = pygame.Rect(
                    x_min + (x_index * size), y_min + (y_index * size), size, size
                )
                pygame.draw.rect(self._display, color, rect)


if __name__ == "__main__":
    if VISUAL:
        theApp = App()
        theApp.on_execute()
    else:
        task.run_day()
