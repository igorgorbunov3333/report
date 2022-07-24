import datetime
import unittest

from report import pomodoro_standard_reporter
from report.model.period_dto import PeriodDto
from report.model.pomodoro_dto import PomodoroDto


class MyTestCase(unittest.TestCase):
    def test_report(self):
        start = datetime.datetime(2022, 7, 18)
        end = datetime.datetime(2022, 7, 24)
        period = PeriodDto(start, end)
        pomodoro_list = self.__prepare_pomodoro_list__()

        actual = pomodoro_standard_reporter.report(period, pomodoro_list, [])

        self.assertEqual(50, actual.standard_amount)  # add assertion here

    def __prepare_pomodoro_list__(self):
        pomodoro = []

        first_day = datetime.datetime(2022, 7, 18)
        pomodoro.extend(self.__build_daily_pomodoro__(first_day))

        second_day = datetime.datetime(2022, 7, 19)
        pomodoro.extend(self.__build_daily_pomodoro__(second_day))

        third_day = datetime.datetime(2022, 7, 20)
        pomodoro.extend(self.__build_daily_pomodoro__(third_day))

        return pomodoro

    def __build_daily_pomodoro__(self, day):
        pomodoro1 = self.__build_single_pomodoro__(day.replace(hour=7), day.replace(hour=7, minute=20))
        pomodoro2 = self.__build_single_pomodoro__(day.replace(hour=8), day.replace(hour=8, minute=20))
        pomodoro3 = self.__build_single_pomodoro__(day.replace(hour=9), day.replace(hour=9, minute=20))
        return [pomodoro1, pomodoro2, pomodoro3]

    @staticmethod
    def __build_single_pomodoro__(start, end):
        return PomodoroDto(start, end, False, [])


if __name__ == '__main__':
    unittest.main()
