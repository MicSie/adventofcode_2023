import day11.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day11(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day11.txt"))

    def test_part1(self):
        self.assertEqual(374, task.sum_shortes_routes(self.input_lines, 2))

    def test_part2(self):
        self.assertEqual(1030, task.sum_shortes_routes(self.input_lines, 10))
        self.assertEqual(8410, task.sum_shortes_routes(self.input_lines, 100))

    def test_expand(self):
        expected = basics.read_file(os.path.abspath("tests/inputs/day11_r.txt"))
        result = task.expand(self.input_lines)
        self.assertEqual(expected, result)

    def test_find_galaxies(self):
        galaxies = task.find_galaxies(task.expand(self.input_lines))
        self.assertEqual(9, len(galaxies))

    def test_get_range(self):
        galaxies = task.find_galaxies(task.expand(self.input_lines))
        self.assertEqual(9, task.get_range(galaxies[4], galaxies[8]))
        self.assertEqual(15, task.get_range(galaxies[0], galaxies[6]))
        self.assertEqual(17, task.get_range(galaxies[2], galaxies[5]))
        self.assertEqual(5, task.get_range(galaxies[7], galaxies[8]))

        galaxies = task.find_galaxies(self.input_lines)
        expansions = task.expands(self.input_lines)
        self.assertEqual(9, task.get_range(galaxies[4], galaxies[8], expansions, 1))
        self.assertEqual(15, task.get_range(galaxies[0], galaxies[6], expansions, 1))
        self.assertEqual(17, task.get_range(galaxies[2], galaxies[5], expansions, 1))
        self.assertEqual(5, task.get_range(galaxies[7], galaxies[8], expansions, 1))


if __name__ == "__main__":
    unittest.main()
