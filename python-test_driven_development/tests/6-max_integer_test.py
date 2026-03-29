#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        """Test an already sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is the first element"""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 8, 3, 4]), 8)

    def test_negative_numbers(self):
        """Test a list of negative numbers"""
        self.assertEqual(max_integer([-4, -2, -8, -1]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 2, 7, -3]), 7)

    def test_repeated_numbers(self):
        """Test a list with repeated max values"""
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)

    def test_float_numbers(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.2, 3.5, 2.8]), 3.5)

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer("Bashar"), "s")

    def test_list_of_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["a", "z", "m", "b"]), "z")


if __name__ == "__main__":
    unittest.main()
