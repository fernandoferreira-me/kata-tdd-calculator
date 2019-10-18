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


class NegativeNotAllowed(Exception):
    pass


class StringCalculator(object):
    """
    Class for implementing a calculator based on strings
    """
    def _filter_negative(self, numbers_list):
        negative_numbers = [n for n in numbers_list if n < 0]
        if negative_numbers:
            raise NegativeNotAllowed('Numbers %s '
                                     'not allowed' % negative_numbers)
        return negative_numbers

    def _add(self, numbers_string, delimiters_list):
        """
        The add function of the calculator
        """
        delimiters = '|'.join(delimiters_list)
        if numbers_string == '':
            return 0
        numbers_list = [int(n) for n in re.split(delimiters, numbers_string)]
        self._filter_negative(numbers_list)
        return sum(numbers_list)

    def add(self, numbers_string):
        """
        The add function of the calculator
        """
        delimiters = [',', '\n']
        if numbers_string[0:2] == '//':
            delimiters = [numbers_string[2]]
            numbers_string = numbers_string[4:]
        return self._add(numbers_string, delimiters)


class ExtendedTestCase(unittest.TestCase):
    def AssertRaisesWithMessage(self, exception, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.fail()
        except exception as exception_msg:
            if str(exception_msg) != msg:
                self.fail(exception_msg)
            pass
        except:
            self.fail()


class TestStringCalculator(ExtendedTestCase):
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

    def testCustomDelimiters(self):
        self.assertEqual(self.calculator.add('//;\n1;2'), 3)

    def testNegativeNumbers(self):
        self.assertRaises(NegativeNotAllowed,
                            self.calculator.add,
                            '-1,2')

    def testMultipleNegativeNumbers(self):
        self.assertRaises(NegativeNotAllowed,
                          self.calculator.add,
                          '-1,-2')

    def testNegativeNumbersNotAllowedMessage(self):
        self.AssertRaisesWithMessage(NegativeNotAllowed,
                                     'Numbers [-1, -2] not allowed',
                                     self.calculator.add,
                                     '-1, -2')

    def testNegativeNumberNotAllowedMessage(self):
        self.AssertRaisesWithMessage(NegativeNotAllowed,
                                     'Numbers [-1] not allowed',
                                     self.calculator.add,
                                     '-1')


if __name__ == "__main__":
    unittest.main()

