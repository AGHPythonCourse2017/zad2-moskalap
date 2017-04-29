class Controller:
    """Class responsible for managing task invokes"""

    def __init__(self, task):
        import countit.scripts.strings as ss
        self.task = task
        self.init_file = open(ss.Strings.INIT_CODE, 'r').read()
        self.examined_file = open(ss.Strings.EXAMINED_CODE, 'r')
        self.clean_up_file = open(ss.Strings.CLEAN_UP_CODE, 'r')

    def run(self, n):
        executrion_string = self.init_file.replace('_N_',str(n))

        return lambda: exec(executrion_string)


    def test(self):
        for i in range(0, 6):
            f = self.run(i)
            f()
            print(a)


