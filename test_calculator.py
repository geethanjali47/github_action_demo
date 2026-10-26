import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(6, 4), 10)

    def test_subtract(self):
        self.assertEqual(subtract(6, 4), 2)

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == "__main__":
    unittest.main()
