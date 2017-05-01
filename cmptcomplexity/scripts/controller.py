class Controller:
    """Class responsible for managing task invokes and returning results"""

    def __init__(self, task, timeout=30):
        self.task = task
        self.timeout = timeout

    def get_data(self):
        """Functions, which invokes timeit, collects data and sends to solver"""

        import signal

        from cmptcomplexity.scripts.decorators import timeout

        @timeout()
        def avrg_measure(task, N, repeat, n):
            import timeit
            list = timeit.repeat(task.stringify_example_invoke(N), task.stringify_init(N), repeat=repeat, number=n)

            return (sum(list) / len(list)) / n

        timeout = self.timeout
        signal.setitimer(signal.ITIMER_REAL, timeout)
        import logging
        can = True
        import random
        MIN = 10
        MAX = 100
        x = []
        y = []
        r = 5
        n = 10
        timeo = 0.00001
        while can:
            if timeo == 0:
                timeo = 0.00001
            i = random.randint(MIN, MAX)
            logging.info('Checking time for N=%s range (0, %s)\nRemainging time=%fs', str(i), str(MAX), timeo,
                         str((timeout - timeo) / float((timeo))))
            timeout = timeo

            c_y, timeo = avrg_measure(self.task, i, r, n)
            if timeo == 'except':
                can = False
            else:

                if timeo > 0.5:
                    if (timeout - timeo) / float((timeo)) < 0.1:
                        MAX = i + MAX
                        n += 1
                    else:
                        if n > 10:
                            n -= 1
                        if MAX > 100:
                            MAX //= 10

                    x.append(i)
                    logging.info('to run alarm %s', str(timeo))
                    y.append(c_y * 1000)
                else:
                    can = False

        ltou, _ = signal.setitimer(signal.ITIMER_REAL, 0)

        import cmptcomplexity.scripts.solver as solver
        slvr = solver.Solver(x, y)
        results = slvr.solve()

        return results
