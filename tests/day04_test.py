import day04.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day04(unittest.TestCase):
    def read_test_input(self) -> list[str]:
        return basics.read_file(os.path.abspath("tests/inputs/day04.txt"))

    def get_parsed_lines(self) -> list[tuple]:
        return task.parse_lines(self.read_test_input())

    def test_part1(self):
        value = task.calculate_value(self.get_parsed_lines())
        self.assertEqual(13, value)

    def test_part2(self):
        value = task.count_cards(self.get_parsed_lines())
        self.assertEqual(30, value)

    def test_parse_line(self):
        line = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
        result = task.parse_line(line)
        self.assertEqual(3, result[0])
        self.assertEqual(5, len(result[1]))
        self.assertEqual(8, len(result[2]))


if __name__ == "__main__":
    unittest.main()
