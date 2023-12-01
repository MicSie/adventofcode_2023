import basics.helpers as helpers   # The code to test

import unittest   # The test framework
import os


class Test_Basics(unittest.TestCase):
    def test_read_file_striped(self):
        path = os.path.abspath('tests/inputs/simpletestfile')
        self.assertEqual(helpers.read_file(path), [
            'first', '2dn', '', '4th'])

    def test_read_file(self):
        path = os.path.abspath('tests/inputs/simpletestfile')
        self.assertEqual(helpers.read_file(path, False), [
            'first', '2dn', '   ', '4th'])


if __name__ == '__main__':
    unittest.main()
