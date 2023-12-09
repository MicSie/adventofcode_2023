import day08.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day08(unittest.TestCase):
    def setUp(self):
        self.input_lines1 = basics.read_file(
            os.path.abspath("tests/inputs/day08_1.txt")
        )
        self.input_lines2 = basics.read_file(
            os.path.abspath("tests/inputs/day08_2.txt")
        )
        self.input_lines3 = basics.read_file(
            os.path.abspath("tests/inputs/day08_3.txt")
        )

    def test_part1(self):
        data = task.parse(self.input_lines1)
        self.assertEqual(2, task.count_steps(data[0], data[1], "AAA", "ZZZ"))
        data = task.parse(self.input_lines2)
        self.assertEqual(6, task.count_steps(data[0], data[1], "AAA", "ZZZ"))

    def test_part2(self):
        data = task.parse(self.input_lines3)
        self.assertEqual(6, task.count_all_steps(data, "A", "Z"))

    def test_parse_lines(self):
        instructions, nodes = task.parse(self.input_lines1)
        self.assertEqual("RL", instructions)
        self.assertEqual(7, len(nodes))
        self.assertEqual(("ZZZ", "GGG"), nodes["CCC"])


if __name__ == "__main__":
    unittest.main()
