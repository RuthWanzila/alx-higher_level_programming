#!/usr/bin/python3
"""
This script tests the max_integer function from the 6-max_integer module.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A test case class for testing the max_integer function.
    """

    def test_upper(self):
        """
        Test case to check if the max_integer function returns the correct maximum value.
        """
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_none(self):
        """
        Test case to check if the max_integer function returns None for an empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """
        Test case to check if the max_integer function returns the correct maximum value for a list with one element.
        """
        self.assertEqual(max_integer([2]), 2)

    def test_one_neg(self):
        """
        Test case to check if the max_integer function returns the correct maximum value for a list with one negative element.
        """
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        """
        Test case to check if the max_integer function returns the correct maximum value for a list with negative elements.
        """
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        """
        Test case to check if the max_integer function returns the correct maximum value for a list with multiple elements.
        """
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)

if __name__ == '__main__':
    unittest.main()

# The crux of each test is a call to assertEqual() to check for an expected result;
# assertTrue() or assertFalse() to verify a condition;
# or assertRaises() to verify that a specific exception gets raised.
# These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.
