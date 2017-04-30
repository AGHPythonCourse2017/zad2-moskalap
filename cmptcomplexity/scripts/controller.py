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
        def timeout():
            def decorator(func):
                def _handle_timeout(signum, frame):
                    raise exceptions.TimeoutCCExcetion('ops')

                def wrapper(*args, **kwargs):
                    ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)
                    signal.setitimer(signal.ITIMER_REAL, ltou)
                    signal.signal(signal.SIGALRM, _handle_timeout)

                    try:
                        result = func(*args, **kwargs)
                    except exceptions.TimeoutCCExcetion:
                        return 0, 'except'

                    finally:
                        ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)
                        signal.setitimer(signal.ITIMER_REAL, ltou)

                    return result, ltou

                return wraps(func)(wrapper)

            return decorator
        @timeout()
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
        timeout = 50
        signal.setitimer(signal.ITIMER_REAL, timeout)
        import logging
        can= True
        import random
        MIN =10
        MAX =100

        timeo = 0.00001
        while can:
            if timeo == 0:
                timeo=0.00001
            i = random.randint(MIN, MAX)
            logging.info('i= %s MAX= %s timeo =%f diff= %s', str(i), str(MAX), timeo,
                         str((timeout - timeo) / float((timeo))))
            timeout=timeo

            c_y, timeo = avrg_measure(self.task,i, 5,10)
            if timeo == 'except':
                can = False
            else:
                if(timeo>0):
                    if (timeout-timeo)/float((timeo)) < 0.1:
                        MAX = i + MAX
                    else:
                        if MAX>100:
                            MAX=MAX//10

                    x.append(i)
                    logging.info('to run alarm %s', str(timeo))
                    y.append(c_y)
                    a_lin.append(c_y / i)
                    a_x2.append(c_y / (i ** 2))
                    a_log.append(c_y / (i * math.log2(i)))

        ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)




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
        q = [(x - y)**2 for x, y in zip(y,quy)]
        print ('y/x^2', sum(q)/len(q),q)
        l = [(x - y)**2 for x, y in zip(y,liny)]
        print ('y/x', sum(l)/len(l),l)
        lg = [(x - y)**2 for x, y in zip(y,logy)]
        print ('y/xlogx', sum(lg)/len(lg),lg)
        plt.plot(x, y, x, liny, x, logy,x,quy)
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



