from report.calculator.work_standard_amount_calculator import calculate_work_standard_amount
from report.model.work_time_standard_report_dto import WorkTimeStandardReportDto


def calculate(period, pomodoro_amount, day_offs):
    standard_amount = calculate_work_standard_amount(period, day_offs)
    balance_amount = pomodoro_amount - standard_amount

    return WorkTimeStandardReportDto(standard_amount, balance_amount, pomodoro_amount)
