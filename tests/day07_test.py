import day07.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day07(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day07.txt"))

    def test_part1(self):
        self.assertEqual(6440, task.get_winnings(self.input_lines, False))

    def test_part2(self):
        self.assertEqual(5905, task.get_winnings(self.input_lines, True))

    def test_get_type_part1(self):
        self.assertEqual(task.FIVE_OF_KIND, task.get_type("AAAAA", False))
        self.assertEqual(task.FOUR_OF_KIND, task.get_type("AA8AA", False))
        self.assertEqual(task.FULL_HOUSE, task.get_type("23332", False))
        self.assertEqual(task.THREE_OF_KIND, task.get_type("TTT98", False))
        self.assertEqual(task.TWO_PAIR, task.get_type("23432", False))
        self.assertEqual(task.ONE_PAIR, task.get_type("A23A4", False))
        self.assertEqual(task.HIGH_CARD, task.get_type("23456", False))

    def test_get_type_part2(self):
        self.assertEqual(task.FIVE_OF_KIND, task.get_type("AAAAA", True))
        self.assertEqual(task.FIVE_OF_KIND, task.get_type("AJAJA", True))
        self.assertEqual(task.FIVE_OF_KIND, task.get_type("JJJJJ", True))

        self.assertEqual(task.FOUR_OF_KIND, task.get_type("AA8AA", True))
        self.assertEqual(task.FOUR_OF_KIND, task.get_type("AA8JJ", True))

        self.assertEqual(task.FULL_HOUSE, task.get_type("23332", True))
        self.assertEqual(task.FULL_HOUSE, task.get_type("23J32", True))

        self.assertEqual(task.THREE_OF_KIND, task.get_type("TTT98", True))
        self.assertEqual(task.THREE_OF_KIND, task.get_type("TJT98", True))

        self.assertEqual(task.TWO_PAIR, task.get_type("23432", True))

        self.assertEqual(task.ONE_PAIR, task.get_type("A23A4", True))
        self.assertEqual(task.ONE_PAIR, task.get_type("J23A4", True))

        self.assertEqual(task.HIGH_CARD, task.get_type("23456", True))


if __name__ == "__main__":
    unittest.main()
