from threading import Thread, Event
import time


class Controller:
    def __init__(self,task, timeout):
        self.task = task
        self.timeout = timeout
        self.run = True


    def simple_task(self, started_evt):
        print('Przed odliczaniem')
        started_evt.set()
        while self.run:
            print('działam')

    def analyze(self):

        started_evt = Event()
        t = Thread(target=self.simple_task, args=(started_evt,))
        t.start()

        started_evt.wait()
        time.sleep(self.timeout)

        if t.is_alive():
            self.run=False

c = Controller(3,12)
c.analyze()