import basics.helpers as helpers  # The code to test

import unittest  # The test framework
import os


class Test_Basics(unittest.TestCase):
    def test_read_file_striped(self):
        path = os.path.abspath("tests/inputs/simpletestfile")
        self.assertEqual(helpers.read_file(path), ["first", "2dn", "", "4th"])

    def test_read_file(self):
        path = os.path.abspath("tests/inputs/simpletestfile")
        self.assertEqual(helpers.read_file(path, False), ["first", "2dn", "   ", "4th"])

    def test_are_ranges_intersecting(self):
        base_range = (10, 20)
        self.assertTrue(helpers.are_ranges_intersecting(base_range, base_range), "same")
        self.assertFalse(helpers.are_ranges_intersecting(base_range, (9, 9)), "before")
        self.assertFalse(helpers.are_ranges_intersecting(base_range, (21, 21)), "after")
        self.assertTrue(
            helpers.are_ranges_intersecting(base_range, (14, 15)),
            "smaller complete inside",
        )
        self.assertTrue(
            helpers.are_ranges_intersecting(base_range, (9, 11)), "smaller reaching in"
        )
        self.assertTrue(
            helpers.are_ranges_intersecting(base_range, (19, 21)),
            "smaller reaching out",
        )
        self.assertTrue(
            helpers.are_ranges_intersecting(base_range, (9, 10)),
            "edges same in",
        )
        self.assertTrue(
            helpers.are_ranges_intersecting(base_range, (19, 20)),
            "edges same out",
        )
        self.assertTrue(helpers.are_ranges_intersecting(base_range, (0, 30)), "larger")


if __name__ == "__main__":
    unittest.main()
