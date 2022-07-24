from datetime import timedelta
from report.util import report_util


def calculate_work_standard_amount(period, day_offs):
    start_date = period.start
    end_date = period.end

    standard_days = []
    for current_date in __date_range__(start_date, end_date):
        week_day_number = current_date.isoweekday()
        if week_day_number != 6 and week_day_number != 7 and current_date not in day_offs:
            standard_days.append(current_date)

    days_amount_to_calculate_standard = len(standard_days)
    return days_amount_to_calculate_standard * report_util.WORK_AMOUNT_STANDARD


def __date_range__(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
