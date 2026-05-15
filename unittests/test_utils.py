import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.utils import clean_text, add_numbers, average, is_in_range

class TestUtils(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("  Hello, World!  "), "hello, world!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([]), 0.0)

    def test_is_in_range(self):
        self.assertTrue(is_in_range(5, 1, 10))
        self.assertFalse(is_in_range(0, 1, 10))
        self.assertTrue(is_in_range(10, 1, 10))

if __name__ == '__main__':
    unittest.main()