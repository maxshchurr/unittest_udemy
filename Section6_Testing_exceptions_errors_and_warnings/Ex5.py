import unittest


def get_average_grade(grades):
    if not isinstance(grades, dict):
        raise TypeError("Input must be a dictionary")
    if not all(isinstance(key, str) for key in grades.keys()):
        raise TypeError("Keys must be strings")
    if not all(
        isinstance(value, (int, float)) for value in grades.values()
    ):
        raise TypeError("Values must be numbers")
    if not grades:
        raise ValueError("Dictionary cannot be empty")
    return sum(grades.values()) / len(grades)


# Enter your solution here
class TestGetAverageGrade(unittest.TestCase):
    def test_empty_dict(self):
        with self.assertRaises(ValueError):
            get_average_grade({})


    def test_non_string_keys(self):
        with self.assertRaises(TypeError):
            get_average_grade({1: 1})

        with self.assertRaises(TypeError):
            get_average_grade({5.5: 5.5})


    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            get_average_grade({1: 'test1'})

        with self.assertRaises(TypeError):
            get_average_grade({2: ['test2', 'test2.1']})

