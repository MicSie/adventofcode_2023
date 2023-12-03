import day02.task as task  # The code to test
import unittest  # The test framework
import os


class Test_Day02(unittest.TestCase):
    def test_part1(self):
        path = os.path.abspath("tests/inputs/day02")
        sum = task.get_possible_sum(path, (14, 13, 12))  # b,g,r
        self.assertEqual(8, sum)

    def test_part2(self):
        path = os.path.abspath("tests/inputs/day02")
        power = task.get_power(path)
        self.assertEqual(2286, power)

    def test_line_read(self):
        input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        result = task.read_line(input)
        self.assertEqual(4, len(result))
        self.assertEqual(1, result[0])  # ID
        self.assertEqual(6, result[1])  # max blue
        self.assertEqual(2, result[2])  # max green
        self.assertEqual(4, result[3])  # max red


if __name__ == "__main__":
    unittest.main()
