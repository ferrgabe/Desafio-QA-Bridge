class TestResult:

    def __init__(self, name, success, duration, message=""):
        self.name = name
        self.success = success
        self.duration = duration
        self.message = message