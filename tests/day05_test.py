import day05.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day05(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day05.txt"))

    def test_part1(self):
        mapping = task.Mapping(self.input_lines)
        self.assertEqual(35, mapping.get_lowest_location_simple())

    def test_part2(self):
        mapping = task.Mapping(self.input_lines)
        self.assertEqual(46, mapping.get_lowest_location_range())

    def test_read_seeds(self):
        expected = {79, 14, 55, 13}
        seeds = set(task.read_seeds(self.input_lines[0]))
        self.assertTrue(seeds == expected)

    def test_read_mapping(self):
        lines = self.input_lines[2:5]
        expected_mapping = {
            (range(98, 100), range(50, 52)),
            (range(50, 50 + 48), range(52, 52 + 48)),
        }
        (mapping, read) = task.read_mapping(lines)
        self.assertEqual(len(lines), read)
        self.assertTrue(expected_mapping == mapping)

    def test_read_from_mapping(self):
        mapping = set({(range(98, 100), range(50, 52))})
        self.assertEqual(50, task.read_from_mapping(mapping, 98))
        self.assertEqual(51, task.read_from_mapping(mapping, 99))
        self.assertEqual(10, task.read_from_mapping(mapping, 10))

    def test_location_to_seed(self):
        mapping = task.Mapping(self.input_lines)
        self.assertEqual(82, mapping.get_location_from_seed(79))
        self.assertEqual(43, mapping.get_location_from_seed(14))
        self.assertEqual(86, mapping.get_location_from_seed(55))
        self.assertEqual(35, mapping.get_location_from_seed(13))

    def test_get_location_from_seedrange(self):
        mapping = task.Mapping(self.input_lines)
        self.assertEqual(
            82, mapping.get_location_ranges_from_seedrange(range(79, 79)).pop().start
        )
        self.assertEqual(
            43, mapping.get_location_ranges_from_seedrange(range(14, 14)).pop().start
        )
        self.assertEqual(
            86, mapping.get_location_ranges_from_seedrange(range(55, 55)).pop().start
        )
        self.assertEqual(
            35, mapping.get_location_ranges_from_seedrange(range(13, 13)).pop().start
        )

    def test_compress_ranges(self):
        expected_mapping = {range(10, 20)}
        self.assertTrue(
            expected_mapping == task.compress_ranges({range(10, 15), range(15, 20)}),
            "neighbours",
        )
        self.assertTrue(
            expected_mapping == task.compress_ranges({range(10, 18), range(12, 20)}),
            "intersection",
        )
        self.assertTrue(
            expected_mapping == task.compress_ranges({range(10, 20), range(12, 14)}),
            "complete inside",
        )

        expected_mapping = {range(5, 9), range(12, 20)}
        self.assertTrue(
            expected_mapping == task.compress_ranges(expected_mapping), "do nothing"
        )

        expected_mapping = {range(5, 9), range(10, 20)}
        self.assertTrue(
            expected_mapping
            == task.compress_ranges(
                task.compress_ranges({range(10, 20), range(12, 14), range(5, 9)})
            ),
            "compresse leave one",
        )


if __name__ == "__main__":
    unittest.main()
