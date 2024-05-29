import unittest
from .calculator import *

global PARAMS

load_params()


class MyTestCase(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculate(1.0, 4, '*', **PARAMS), 4)  # Проверка операции умножения

    def test_sum(self):
        self.assertEqual(calculate(1, 2, "+", **PARAMS), 3)

    def test_divide(self):
        self.assertEqual(calculate(7, 3, '//', **PARAMS), 2)

    def test_mod(self):
        self.assertEqual(calculate(9, 2, "%", **PARAMS), 1)

    def test_standard_deviation(self):
        self.assertEqual(standard_deviation(45, 45, 32, 65, 999, **PARAMS), 381.04614)

    def test_cp_with_1(self):
        self.assertEqual(convert_precision('0.1'), 1, "Должна быть 1")

    def test_cp_with_2(self):
        self.assertEqual(convert_precision('0.01'), 2, "Должно быть 2")

    def test_cp_with_5(self):
        self.assertEqual(convert_precision('0.00001'), 5, "Должно быть 5")

    def test_cp_with_5_as_float(self):
        self.assertEqual(convert_precision(0.00001), 5, "Должно быть 5")
