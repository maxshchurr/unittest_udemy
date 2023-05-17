import unittest


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height

# Enter your solution here
class TestRectangle(unittest.TestCase):

    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height


class TestRectangle(unittest.TestCase):
    def test_area_with_nonzero_dimensions(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_area_with_zero_dimensions(self):
        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.area(), 0)

    def test_area_with_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-4, 5)

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(4, -5)

    def test_area_with_float_dimensions(self):
        rectangle = Rectangle(3.5, 2.5)
        self.assertEqual(rectangle.area(), 8.75)

    def test_area_with_large_dimensions(self):
        rectangle = Rectangle(1000000, 1000000)
        self.assertEqual(rectangle.area(), 1000000000000)