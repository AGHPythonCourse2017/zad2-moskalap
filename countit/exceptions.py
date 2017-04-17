class InitializationError:
    def __init__(self, val):
        self.val=val

    def __str__(self):
        return self.val


class ArgumentPatternError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class AnalyzablePatternError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val