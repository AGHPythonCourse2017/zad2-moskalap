class Controller:
    """Class responsible for managing task invokes and returning results"""

    def __init__(self, task, timeout):
        self.task = task
        self.timeout = timeout
    def get_data(self):
        """Functions, which invokes timeit and collects data from it"""
        from functools import wraps
        import errno
        import os
        import signal
        import cmptcomplexity.scripts.exceptions as exceptions
        def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
            def decorator(func):
                def _handle_timeout(signum, frame):
                    raise exceptions.TimeoutCCExcetion(error_message)

                def wrapper(*args, **kwargs):
                    signal.signal(signal.SIGALRM, _handle_timeout)
                    signal.alarm(seconds)
                    try:
                        result = func(*args, **kwargs)
                    finally:
                        signal.alarm(0)
                    return result

                return wraps(func)(wrapper)

            return decorator

        def avrg_measure(task, N, repeat, n):
            import timeit
            list = timeit.repeat(task.stringify_example_invoke(N), task.stringify_init(N), repeat=repeat, number=n)

            return (sum(list)/len(list))/n


        x = []
        y = []
        liny = []
        quy = []
        logy = []
        a_lin = []
        a_x2 = []
        a_log = []
        import math
        for i in [10,100,1000,10000,100000,1000000]:

            x.append(i) #firstmeasure
            c_y = avrg_measure(self.task,i, 5,10)
            y.append(c_y)
            a_lin.append(c_y / i)
            a_x2.append(c_y / (i ** 2))
            a_log.append(c_y / (i * math.log2(i)))






        import matplotlib.pyplot as plt

        a_ratio = sum(a_lin) / len(a_lin)
        ax2_ratio = sum(a_x2) / len(a_x2)
        alog = a_log[0]/ 1

        for act_x in x:
            quy.append(ax2_ratio * (act_x ** 2))
            liny.append(a_ratio* act_x)
            logy.append(alog*math.log2(act_x) * act_x)

        print('x', x)
        print('y', y)
        print('x^2',quy)
        print('x',liny)
        print('xlogx',logy)
        print ('y/x^2', [x / y for x, y in zip(y,quy)])
        print ('y/x', [x / y for x, y in zip(y,liny)])
        print ('y/xlogx', [x / y for x, y in zip(y,logy)])
        plt.plot(x, y, x, liny, x, logy)
        plt.show()









    def run(self, n):
        executrion_string = self.init_file.replace('_N_',str(n))

        return lambda: exec(executrion_string)

    def get_results(self):
        class Result:
            def __init__(self, x,y,complexity,how_long = None, how_many = None):
                self.x = x
                self.y = y
                self.complexity = complexity
                self.how_long = how_long
                self.how_many = how_many

            def stringify_results(self):
                return tuple(iter(self.x, self.y))



