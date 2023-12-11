import day10.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day10(unittest.TestCase):
    def test_part1(self):
        maze = task.MazeHolder(os.path.abspath("tests/inputs/day10_1.txt"))
        self.assertEqual(4, maze.get_steps_to_farthest_point())
        maze = task.MazeHolder(os.path.abspath("tests/inputs/day10_2.txt"))
        self.assertEqual(8, maze.get_steps_to_farthest_point())

    def test_part2(self):
        maze = task.MazeHolder(os.path.abspath("tests/inputs/day10_3.txt"))
        self.assertEqual(4, maze.count_inside_cells())
        maze = task.MazeHolder(os.path.abspath("tests/inputs/day10_4.txt"))
        self.assertEqual(8, maze.count_inside_cells())
        maze = task.MazeHolder(os.path.abspath("tests/inputs/day10_5.txt"))
        self.assertEqual(10, maze.count_inside_cells())


if __name__ == "__main__":
    unittest.main()
