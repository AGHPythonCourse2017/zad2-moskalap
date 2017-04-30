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

        self.initialize()
         #count *
         #fork

        started_evt = Event()
        t = Thread(target=self.simple_task, args=(started_evt,))
        t.start()

        started_evt.wait()
        time.sleep(self.timeout)

        if t.is_alive():
            self.run=False

    def initialize(self):
        #init


class Task():
    def __init__(self, initialization_code, analyzable, clean_up = None):
        self.initalization_code = initialization_code
        self.analyzable = analyzable
        self.clean_up = clean_up
        self.initialize_structures
c = Controller(3,12)
c.analyze()