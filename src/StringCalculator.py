#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 fguimara <fguimara@Fernandos-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""
Kata TDD String Calculator
"""

import unittest
import re


class StringCalculator(object):
    """
    Class for implementing a calculator based on strings
    """
    def add(self, numbers_string):
        """
        The add function of the calculator
        """
        delimiters = ',|\n'
        if numbers_string == '':
            return 0
        numbers_list = [int(n) for n in re.split(delimiters, numbers_string)]
        return sum(numbers_list)



class TestStringCalculator(unittest.TestCase):
    """
    Tests for strings
    """
    def setUp(self):
        self.calculator = StringCalculator()

    def testEmptyString(self):
        self.assertEqual(self.calculator.add(''), 0)

    def testOneNumberString(self):
        self.assertEqual(self.calculator.add('1'), 1)

    def testTwoNumbersString(self):
        self.assertEqual(self.calculator.add('1,2'), 3)

    def testSeveralNumbersString(self):
        self.assertEqual(self.calculator.add('1,2,3,4'), 10)

    def testNewLineDelimiter(self):
        self.assertEqual(self.calculator.add('1\n2,3'), 6)



if __name__ == "__main__":
    unittest.main()

