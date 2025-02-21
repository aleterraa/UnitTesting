import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathUtils.add(1, 2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        self.assertEqual(MathUtils.subtract(1, 2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1.0)
        self.assertEqual(MathUtils.subtract(-1, 1), -2)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), -3.0)

    def test_divide(self):
        self.assertEqual(MathUtils.divide(1, 2), 0.5)
        self.assertEqual(MathUtils.divide(1.5, 2.5), 0.6)
        self.assertEqual(MathUtils.divide(-1, 1), -1)
        self.assertEqual(MathUtils.divide(-1.5, 1.5), -1)

    def test_multiply(self):
        self.assertEqual(MathUtils.multiply(1, 2), 2)
        self.assertEqual(MathUtils.multiply(1.5, 2.5), 3.75)
        self.assertEqual(MathUtils.multiply(-1, 1), -1)
        self.assertEqual(MathUtils.multiply(-1.5, 1.5), -2.25)

    def test_pow(self):
        self.assertEqual(MathUtils.pow(1, 2), 1)
        self.assertEqual(MathUtils.pow(2, 3), 8)
        self.assertEqual(MathUtils.pow(-7, 2), 49)
        self.assertEqual(MathUtils.pow(-4, 3), -64)