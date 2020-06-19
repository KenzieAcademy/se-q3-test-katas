import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(22, katas.add(10, 12))
        self.assertNotEqual(120, katas.add(10, 12))

    def test_multiply(self):
        self.assertEqual(120, katas.multiply(10, 12))
        self.assertNotEqual(22, katas.multiply(10, 12))

    def test_power(self):
        self.assertEqual(32, katas.power(2, 5))
        self.assertNotEqual(10, katas.power(2, 5))
        self.assertNotEqual(7, katas.power(2, 5))

    def test_factorial(self):
        self.assertEqual(120, katas.factorial(5))
        self.assertEqual(3628800, katas.factorial(10))

    def test_fibonacci(self):
        self.assertEqual(0, katas.fibonacci(1))
        self.assertEqual(1, katas.fibonacci(2))
        self.assertEqual(1, katas.fibonacci(3))
        self.assertEqual(28657, katas.fibonacci(24))


if __name__ == '__main__':
    unittest.main()
