import day09.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day09(unittest.TestCase):
    def setUp(self):
        self.input_lines = task.parse(
            basics.read_file(os.path.abspath("tests/inputs/day09.txt"))
        )

    def test_part1(self):
        self.assertEqual(
            114, sum([task.predict(line, True) for line in self.input_lines])
        )

    def test_part2(self):
        self.assertEqual(
            2, sum([task.predict(line, False) for line in self.input_lines])
        )

    def test_get_differences(self):
        self.assertEqual(
            {3, 3, 3, 3, 3}, set(task.get_differences(self.input_lines[0]))
        )

    def test_predict(self):
        self.assertEqual(18, task.predict(self.input_lines[0], True))
        self.assertEqual(28, task.predict(self.input_lines[1], True))
        self.assertEqual(68, task.predict(self.input_lines[2], True))
        self.assertEqual(5, task.predict(self.input_lines[2], False))


if __name__ == "__main__":
    unittest.main()
