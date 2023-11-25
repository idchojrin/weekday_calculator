import unittest

import datetime

import week_day_calculator


class WeekDayCalculatorTest(unittest.TestCase):
    def test_should_calculate_week_day_for_given_date(self):
        self.assertEqual("Saturday", week_day_calculator.week_day_for(datetime.datetime(2023, 10, 7)))
        self.assertEqual("Sunday", week_day_calculator.week_day_for(datetime.datetime(2023, 10, 1)))
        self.assertEqual("Tuesday", week_day_calculator.week_day_for(datetime.datetime(2015, 3, 3)))
        self.assertEqual("Thursday", week_day_calculator.week_day_for(datetime.datetime(1977, 12, 22)))

if __name__ == '__main__':
    unittest.main()
