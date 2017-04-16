class Controller:
    def __init__(self, task, timeout):
        self.timeout = timeout

    def run_task(self):
        import time
        time.sleep(10)

    def start(self):
        from threading import Thread
        t = Thread (target=self.run_task())
        t.start()
        while(t.is_alive()):
            print("żyje")





c=Controller
c.run_task()