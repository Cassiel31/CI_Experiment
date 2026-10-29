import unittest
from calculator import add


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_addition_with_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_addition_of_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
