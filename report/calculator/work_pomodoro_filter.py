from report.util import report_util


def filter_pomodoro(pomodoro):
    return list(filter(
        lambda p: report_util.WORK_POMODORO_TAG in __map_to_tag_names__(p.tags), pomodoro))


def __map_to_tag_names__(tags):
    return list(map(
        lambda t: t.name, tags))
