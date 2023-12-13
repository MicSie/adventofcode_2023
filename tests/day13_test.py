import day13.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day13(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day13.txt"))

    def test_part1(self):
        parsed = task.parse(self.input_lines)
        self.assertEqual(405, task.sum_mirror_lines(parsed))
        self.assertEqual(405, task.sum_mirror_lines_with_error(parsed, 0))

    def test_part2(self):
        parsed = task.parse(self.input_lines)
        self.assertEqual(400, task.sum_mirror_lines_with_error(parsed))

    def test_find_mirror_line_with_error(self):
        data = [
            "#.##..###",
            "..##..#.#",
            "#####.##.",
            "#####.##.",
            "..##..#.#",
            "#.##..###",
        ]
        self.assertEqual(3, task.find_mirror_line_with_error(data))
        data = [
            "#.##..###",
            "..##..#.#",
            "#####.##.",
            "#####.##.",
            "..##..#.#",
            "#.##..#.#",
        ]
        self.assertEqual(3, task.find_mirror_line_with_error(data))
        data = [
            "#.##..###",
            "..##..#.#",
            "#####.##.",
            "#####.##.",
            "..##..#.#",
            "####..###",
        ]
        self.assertEqual(3, task.find_mirror_line_with_error(data))

    def test_parse_input(self):
        expected1 = [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ]

        expected2 = [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#",
        ]

        parsed = task.parse(self.input_lines)
        self.assertEqual(expected1, parsed[0])
        self.assertEqual(expected2, parsed[1])

    def test_rotate(self):
        data = ["123", "456", "789"]
        expected = ["741", "852", "963"]
        result = task.rotate(data)
        self.assertEqual(expected, result)

    def test_find_matching_lines(self):
        data = [
            "#...##..#",  # 0
            "#....#..#",  # 1
            "..##..###",  # 2
            "#####.##.",  # 3
            "#####.##.",  # 4
            "..##..###",  # 5
            "#....#..#",  # 6
        ]

        expected = {
            "#...##..#": [0],
            "#....#..#": [1, 6],
            "..##..###": [2, 5],
            "#####.##.": [3, 4],
        }

        result = task.find_matching_lines(data)
        self.assertEqual(expected, result)

    def test_find_mirror_line(self):
        edge_test = {
            "01": [0],
            "02": [1, 6, 11, 16],
            "03": [2, 5, 12, 15],
            "04": [3, 14],
            "05": [4, 13],
            "06": [7, 10],
            "07": [8, 9],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(8, line)

        edge_test = {
            "01": [0, 5],
            "02": [1],
            "03": [2, 3, 12],
            "04": [4],
            "05": [6],
            "06": [7],
            "07": [8],
            "08": [9],
            "09": [10],
            "11": [11],
            "13": [13],
            "14": [14],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(None, line)

        edge_test = {
            "01": [0, 13, 14],
            "02": [1, 12, 15],
            "03": [2, 11, 16],
            "04": [3, 10],
            "05": [4],
            "06": [5, 8],
            "07": [6, 7],
            "08": [9],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(13, line)

        edge_test = {
            "01": [0],
            "02": [1],
            "03": [2],
            "04": [3],
            "05": [8],
            "06": [9],
            "07": [10],
            "08": [11, 14],
            "09": [12, 13],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(12, line)

        parsed = task.parse(self.input_lines)
        line = task.find_mirror_line(task.find_matching_lines(parsed[0]))
        self.assertEqual(None, line)
        line = task.find_mirror_line(task.find_matching_lines(task.rotate(parsed[0])))
        self.assertEqual(5, line + 1)  # example starts at 1

        line = task.find_mirror_line(task.find_matching_lines(parsed[1]))
        self.assertEqual(4, line + 1)

        edge_test = {
            "#...??..#": [7],
            "#...##..#": [0],
            "#....#..#": [1, 6],
            "..##..###": [2, 5],
            "#####.##.": [3, 4],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(None, line)

        edge_test = {
            "01": [0, 7],
            "02": [1, 6],
            "03": [2, 5],
            "04": [3, 4],
            "05": [8, 13],
            "06": [9, 12],
            "07": [10, 11],
            "08": [14],
        }

        line = task.find_mirror_line(edge_test)
        self.assertEqual(3, line)

        edge_test = {"#...??..#": [7], "#...##..#": [0]}

        line = task.find_mirror_line(edge_test)
        self.assertEqual(None, line)


if __name__ == "__main__":
    unittest.main()
