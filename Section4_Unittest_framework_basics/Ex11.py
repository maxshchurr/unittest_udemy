import unittest


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

# Enter your solution here
class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        temp_conv = TemperatureConverter()
        self.assertAlmostEqual(temp_conv.celsius_to_fahrenheit(10), 50, delta=0.5)
        self.assertAlmostEqual(temp_conv.celsius_to_fahrenheit(0), 32, delta=0.5)
        self.assertAlmostEqual(temp_conv.celsius_to_fahrenheit(110), 230, delta=0.5)

if __name__ == '__main__':
    unittest.main()