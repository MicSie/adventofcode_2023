import day12.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day12(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day12.txt"))

    def test_part1(self):
        self.assertEqual(21, task.sum_arrangements(self.input_lines))

    def test_part2(self):
        self.assertEqual(525152, task.sum_arrangements(self.input_lines, 5))

    def test_get_arrangement_count(self):
        self.assertEqual(1, task.get_arrangement_count(self.input_lines[0]))
        self.assertEqual(4, task.get_arrangement_count(self.input_lines[1]))
        self.assertEqual(1, task.get_arrangement_count(self.input_lines[2]))
        self.assertEqual(1, task.get_arrangement_count(self.input_lines[3]))
        self.assertEqual(4, task.get_arrangement_count(self.input_lines[4]))
        self.assertEqual(10, task.get_arrangement_count(self.input_lines[5]))

    def test_get_arrangement_count_with_multiplier(self):
        self.assertEqual(1, task.get_arrangement_count(self.input_lines[0], 5))
        self.assertEqual(16384, task.get_arrangement_count(self.input_lines[1], 5))
        self.assertEqual(1, task.get_arrangement_count(self.input_lines[2], 5))
        self.assertEqual(16, task.get_arrangement_count(self.input_lines[3], 5))
        self.assertEqual(2500, task.get_arrangement_count(self.input_lines[4], 5))
        self.assertEqual(506250, task.get_arrangement_count(self.input_lines[5], 5))


if __name__ == "__main__":
    unittest.main()
