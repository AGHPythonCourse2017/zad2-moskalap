class Controller:
    """Class responsible for managing task invokes and returning results"""

    def __init__(self, task, timeout):
        self.task = task
        self.timeout = timeout

    def get_data(self):
        """Functions, which invokes timeit and collects data from it"""
        from functools import wraps
        import signal
        import cmptcomplexity.scripts.exceptions as exceptions

        from cmptcomplexity.scripts.decorators import timeout
        from cmptcomplexity.scripts.decorators import log_it

        @log_it
        @timeout()
        def avrg_measure(task, N, repeat, n):
            import timeit
            list = timeit.repeat(task.stringify_example_invoke(N), task.stringify_init(N), repeat=repeat, number=n)

            return (sum(list)/len(list))/n

        timeout = 200
        signal.setitimer(signal.ITIMER_REAL, timeout)
        import logging
        can= True
        import random
        MIN =10
        MAX =100
        x=[]
        y=[]

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

                if(timeo>0.5):
                    if (timeout-timeo)/float((timeo)) < 0.1:
                        MAX = i + MAX
                    else:
                        if MAX>100:
                            MAX=MAX//10

                    x.append(i)
                    logging.info('to run alarm %s', str(timeo))
                    y.append(c_y)
                else:
                    can = False


        ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)

        import cmptcomplexity.scripts.solver as solver
        slvr = solver.Solver(x,y)











    def run(self, n):
        executrion_string = self.init_file.replace('_N_',str(n))

        return lambda: exec(executrion_string)





