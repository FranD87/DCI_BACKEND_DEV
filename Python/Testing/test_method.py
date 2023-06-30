import datetime
import unittest
from freezegun import freeze_time
from method import discount_calculator

# pip install freezegun

class DiscountCalculatorTes(unittest.TestCase):
    @freeze_time('2023-01-01')
    def test_no_discount(self):
        self.assertEqual(100.0, discount_calculator(
            value=100,
            due_data=datetime.date(year=2023, month=1, day=28),
            days=10,
            discount=0.2
        ))
    @freeze_time('2023-01-19')
    def test_discount(self):
        self.assertEqual(80.0, discount_calculator(
            value=100,
            due_data=datetime.date(year=2023, month=3, day=28),
            days=10,
            discount=0.2
        ))



