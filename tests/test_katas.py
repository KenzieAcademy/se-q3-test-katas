import unittest
import katas
import random
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        num1 = random.randrange(8)
        num2 = random.randrange(8)
        negative1 = random.randrange(-8, -1)
        negative2 = random.randrange(-8, -1)
        self.assertEqual(katas.add(num1, num2), num1 + num2)
        self.assertEqual(katas.add(negative1, negative2), negative1 + negative2)

    def test_multiply(self):
        num1 = random.randrange(8)
        num2 = random.randrange(8)
        negative1 = random.randrange(-8, -1)
        negative2 = random.randrange(-8, -1)
        self.assertEqual(katas.multiply(num1, num2), num1 * num2)
        self.assertEqual(katas.multiply(negative1, negative2), negative1 * negative2)

    def test_power(self):
        num1 = random.randrange(8)
        num2 = random.randrange(8)
        negative = random.randrange(-8, -1)
        fractional = random.random()
        self.assertRaises(ValueError, katas.power, num1, negative)
        self.assertRaises(ValueError, katas.power, num1, fractional)
        self.assertEqual(katas.power(num1, num2), pow(num1, num2))

    def test_factorial(self):
        num = 15
        negative = -4
        self.assertRaises(ValueError, katas.factorial, negative)
        self.assertEqual(katas.factorial(num), math.factorial(num))

    def test_fibonacci(self):
        fibonacci = [0, 1]
        count, num1, num2 = 0, 0, 1
        while count < 30:
            new_num = num1 + num2
            fibonacci.append(new_num)
            num1 = num2
            num2 = new_num
        negative = -4
        self.assertRaises(ValueError, katas.fibonacci, negative)
        self.assertListEqual([katas.factorial(1), katas.factorial(2), katas.factorial(3), katas.factorial(4), katas.factorial(5), katas.factorial(6), katas.factorial(7), katas.factorial(8), katas.factorial(9), katas.factorial(10), katas.factorial(11), katas.factorial(12), katas.factorial(13), katas.factorial(14), katas.factorial(15), katas.factorial(16), katas.factorial(17), katas.factorial(18), katas.factorial(19), katas.factorial(20), katas.factorial(21), katas.factorial(22), katas.factorial(23), katas.factorial(24), katas.factorial(25), katas.factorial(26), katas.factorial(27), katas.factorial(28), katas.factorial(29), katas.factorial(30)], fibonacci)

if __name__ == '__main__':
    unittest.main()
