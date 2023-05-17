import unittest


def calculate_daily_return(
    open_price: float, close_price: float
) -> float:
    return round(((close_price / open_price) - 1) * 100, 7)


class TestCalculateDailyReturn(unittest.TestCase):
    pass