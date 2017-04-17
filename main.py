class Controller:
    def __init__(self, task, timeout):
        self.task = task
        self.timeout = timeout

        from threading import Thread
        t = Threadzz
