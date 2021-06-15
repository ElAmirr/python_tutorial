import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(10, 20), -10)
        self.assertEqual(calc.substract(20, 20), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)


if __name__ == '__main__':
    unittest.main()