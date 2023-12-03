import day03.task as task  # The code to test
import unittest  # The test framework
import os


class Test_Day03(unittest.TestCase):
    def test_part1(self):
        path = os.path.abspath("tests/inputs/day03")
        sum = task.get_sum_of_parts(path)
        self.assertEqual(4361, sum)

    def test_part2(self):
        path = os.path.abspath("tests/inputs/day03")
        gear_ratio = task.get_gear_ratio(path)
        self.assertEqual(467835, gear_ratio)

    def test_get_numbers_do_not_get_same_twice(self):
        input = [".118.", ".*...", ".102."]
        result = task.get_numbers(input, 1, 1)
        self.assertEqual(118, result[0])
        self.assertEqual(102, result[1])

    def test_get_numbers_two_numbers_same_line(self):
        input = ["...........123.456.", "..............*....", "................935"]
        result = task.get_numbers(input, 1, 14)
        self.assertEqual(123, result[0])
        self.assertEqual(456, result[1])
        input = ["................935", "..............*....", "...........123.456."]
        result = task.get_numbers(input, 1, 14)
        self.assertEqual(123, result[0])
        self.assertEqual(456, result[1])

    def test_adjacent_to_symbol_corners(self):
        input = ["5..", "+..", "..."]
        result = task.is_adjacent_to_symbol(input, 0, 0, 1)
        self.assertTrue(result)
        input = ["...", "..+", "..5"]
        result = task.is_adjacent_to_symbol(input, 2, 2, 1)
        self.assertTrue(result)

    def test_adjacent_to_symbol_false(self):
        input = ["...", ".5.", "..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertFalse(result)

    def test_adjacent_to_symbol_true_vertical(self):
        input = [".*.", ".5.", "..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)
        input = ["...", ".5.", ".*."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)

    def test_adjacent_to_symbol_true_horizontal(self):
        input = ["...", "*5.", "..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)
        input = ["...", ".5*", "..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)

    def test_adjacent_to_symbol_true_diagonal(self):
        input = ["*..", ".5.", "..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)
        input = ["...", ".5.", "..*"]
        result = task.is_adjacent_to_symbol(input, 1, 1, 1)
        self.assertTrue(result)

    def test_adjacent_to_symbol_false_long(self):
        input = [".....", ".456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertFalse(result)

    def test_adjacent_to_symbol_true_vertical_long(self):
        input = [".*...", ".456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        input = ["..*..", ".456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        input = ["...*.", ".456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)

        input = [".....", ".456.", ".*..."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)
        input = [".....", ".456.", "..*.."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)
        input = [".....", ".456.", "...*."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)

    def test_adjacent_to_symbol_true_horizontal_long(self):
        input = [".....", "*456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)
        input = [".....", ".456*", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)

    def test_adjacent_to_symbol_true_diagonal_long(self):
        input = ["*....", ".456.", "....."]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)
        input = [".....", ".456.", "....*"]
        result = task.is_adjacent_to_symbol(input, 1, 1, 3)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
