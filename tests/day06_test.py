import day06.task as task  # The code to test
import unittest  # The test framework
import os
import basics


class Test_Day06(unittest.TestCase):
    def setUp(self):
        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/day06.txt"))

    def test_part1(self):
        self.assertEqual(
            288, task.beat_record(task.get_times_distances(self.input_lines))
        )

    def test_part2(self):
        self.assertEqual(
            71503, task.get_options_count(task.get_time_distance(self.input_lines))
        )


if __name__ == "__main__":
    unittest.main()
