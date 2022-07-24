from report.calculator import work_pomodoro_filter, work_time_standard_report_calculator


def report(period, pomodoro_list, day_offs):
    work_pomodoro = work_pomodoro_filter.filter_pomodoro(pomodoro_list)
    work_standard_report_dto = work_time_standard_report_calculator.calculate(period, len(work_pomodoro), day_offs)

    return work_standard_report_dto
