import day01.task as task  # The code to test
import unittest  # The test framework
import os


class Test_Day01(unittest.TestCase):
    def test_part1(self):
        path = os.path.abspath("tests/inputs/day01_1.txt")
        calibration_sum = task.read_simple_calibration_sum_from_file(path)
        self.assertEqual(calibration_sum, 142)

    def test_part2(self):
        path = os.path.abspath("tests/inputs/day01_2.txt")
        calibration_sum = task.read_calibration_sum_from_file(path)
        self.assertEqual(calibration_sum, 281)


if __name__ == "__main__":
    unittest.main()
