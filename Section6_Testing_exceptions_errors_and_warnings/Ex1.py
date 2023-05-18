import unittest


def divide(x, y):
    return x / y


# Enter your solution here
class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)