import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
    
    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), -3)

    def test_subtract_plus(self):
        self.assertEqual(self.calc.subtract(4, 18), 14)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(9, 0), -9)

    def test_multi(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multi_zero(self):
        self.assertEqual(self.calc.multiply(0, 6), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 4), 3)
    
    def test_divide_plus(self):
        self.assertEqual(self.calc.divide(125, 5), 25)
    
    def test_divide_unique(self):
        self.assertEqual(self.calc.divide(15, 0), 0)
    
    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0, 63), 0)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(60, 12), 0)

    def test_mod_II(self):
        self.assertEqual(self.calc.modulo(33, 2), 1)

if __name__ == '__main__':
    unittest.main()
