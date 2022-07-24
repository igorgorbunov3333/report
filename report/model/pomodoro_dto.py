

class PomodoroDto:
    def __init__(self, start_time, end_time, save_automatically, tags):
        self.start_time = start_time
        self.end_time = end_time
        self.saveAutomatically = save_automatically
        self.tags = tags
