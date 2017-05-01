class Solver:
    """Class responsible for solving a problem with received data from controller"""

    class Result:
        """Container for a results"""

        def __init__(self, x, y, complexity, sheet):
            self.x = x
            self.y = y
            self.complexity_k = complexity
            self.complexity = {
                'linear_ratios': 'O(N)',
                'square_ratios': 'O(N^2)',
                'xlogx_ratios': 'O(N log N)',
                'logx_ratios': 'O(log N)',
                'constant': 'O(1)'

            }[complexity]
            self.sheet = sheet

            fun_tuple = self.sheet[self.complexity_k]
            import math
            if len(fun_tuple) == 2:
                p1, p2 = fun_tuple

                fun_tuple = (p1, p2, [0])
            print(fun_tuple)

            self.fun = {

                'linear_ratios': (
                    lambda x: fun_tuple[0][0] + x * fun_tuple[1][0],
                    str(fun_tuple[1][0]) + 'N+' + str(fun_tuple[0][0])),
                'square_ratios': (lambda x: fun_tuple[0][0] + x * fun_tuple[1][0] + fun_tuple[2][0] * x ** 2,
                                  str(fun_tuple[2][0]) + 'N^2+' + str(fun_tuple[1][0]) + 'N+' + str(fun_tuple[0][0])),
                'xlogx_ratios': (lambda x: fun_tuple[0][0] * x * math.log2(x) + fun_tuple[1][0] * x,
                                 str(fun_tuple[0][0]) + 'N log(' + str(
                                     math.exp((fun_tuple[1][0] / fun_tuple[0][0]) ** 2)) + 'N)'),
                'logx_ratios': (lambda x: fun_tuple[0][0] + math.log2(x) * fun_tuple[1][0],

                                str(str(fun_tuple[1][0]) + 'log' + str(
                                    math.exp(fun_tuple[1][0] / fun_tuple[0][0])) + str(fun_tuple[0][0]))),
                'constant': (lambda x: sum(self.y) / len(self.y), 'O(1)')
            }[complexity]

        def show(self, title):

            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            import numpy as np
            charts = self.sheet.keys()
            MAX = max(self.y)
            xrange = np.linspace(1, self.x[-1], len(self.x))

            def prepare_chart(key):
                if key != self.complexity_k:
                    if key == 'logx_ratios':
                        values = list(filter(lambda k: k <= MAX, np.log2(xrange) * self.sheet['logx_ratios']))
                        plt.plot(xrange[0:len(values)], values, label='o(log N)', linestyle='--', color='b')
                    if key == 'square_ratios':
                        values = list(filter(lambda k: k <= MAX, np.power(xrange, 2) * self.sheet['square_ratios']))
                        plt.plot(xrange[0:len(values)], values, label='o(N^2)', linestyle='--', color='r')
                    if key == 'xlogx_ratios':
                        values = list(filter(lambda k: k <= MAX, np.log2(xrange) * xrange * self.sheet['xlogx_ratios']))
                        plt.plot(xrange[0:len(values)], values, label='o(N log N)', linestyle='--', color='g')
                    if key == 'logx_ratios':
                        values = list(filter(lambda k: k <= MAX, np.multiply(xrange, self.sheet['linear_ratios'])))
                        plt.plot(xrange[0:len(values)], values, label='o(N)', linestyle='--', color='y')

                else:
                    if key == 'log_xratios':
                        values = list(filter(lambda k: k <= MAX, [sum(self.y) / len(self.y) for i in xrange]))
                        plt.plot(xrange[0:len(values)], values, label='o(1)', linestyle='--', color='y')

                    values = list(filter(lambda k: k <= MAX, [self.fun[0](x) for x in xrange]))
                    plt.plot(xrange[0:len(values)], values, label=self.fun[1], linestyle='--', color='k')

            for x in charts:
                prepare_chart(x)

            plt.plot(self.x, self.y, label='measured times', marker='o', linestyle='', color='k')
            plt.legend()
            plt.title(str(title) + '\n' + self.complexity)

            plt.xlabel('problem size[N]')
            plt.ylabel('time [MSEC]')
            plt.legend(loc=2, prop={'size': 6})
            plt.show()
            plt.savefig(title + '_plot.png', ext='png', bbox_inches='tight', dpi=1200)

    def __init__(self, x, y):

        self.points = []
        self.sheet = {
            'linear_ratios': [],
            'square_ratios': [],
            'xlogx_ratios': [],
            'logx_ratios': [],
            'constant': []

        }
        import math

        for i in range(len(x)):
            self.points.append((x[i], y[i]))

        self.x, self.y = map(list, zip(*sorted(self.points, key=lambda k: k[0])))

        for i in range(len(x)):
            self.sheet.get('linear_ratios').append(self.y[i] / self.x[i])
            self.sheet.get('square_ratios').append(self.y[i] / (self.x[i] ** 2))
            self.sheet.get('xlogx_ratios').append(self.y[i] / (self.x[i] * math.log2(self.x[i])))
            self.sheet.get('logx_ratios').append(self.y[i] / (math.log2(self.x[i])))
            self.sheet.get('constant').append(self.y[i])

    def solve(self):
        # in sheet there are ratios
        the_most_accurate = None
        diff = 999999

        def count_diff(x):
            import math
            avg = sum(x) / len(x)
            diff = 0
            for i in x:
                diff += math.sqrt(((avg - i) / avg) ** 2)
            return diff

        def count_ratio(x):
            return sum(x[1:3]) / len(x[1:3])

        for key in self.sheet.keys():
            new_diff = count_diff(self.sheet.get(key))
            if new_diff < diff:
                if the_most_accurate:
                    self.sheet[the_most_accurate] = count_ratio(self.sheet.get(the_most_accurate))

                the_most_accurate = key
                diff = new_diff
            else:
                self.sheet[key] = count_ratio(self.sheet.get(key))

        import math

        def aproximate_leas_square(base):
            import numpy as np
            base_fun = base[0]

            A = np.matrix([list([base_fun[i](x) for i in range(len(base_fun))]) for x in self.x])

            AT = A.transpose()
            A = np.dot(AT, A)
            b = np.matrix([list([x]) for x in self.y])
            Y = np.dot(AT, b)
            from scipy.linalg import solve
            X = solve(A, Y)

            self.sheet[the_most_accurate] = tuple(X)

        base = {
            # (base, ratios)
            'linear_ratios': ((lambda x: 1, lambda x: x), ('b', 'a')),
            'square_ratios': ((lambda x: 1, lambda x: x, lambda x: x ** 2), ('c', 'b', 'a')),
            'xlogx_ratios': ((lambda x: x * math.log2(x), lambda x: x), ('a', 'alogb')),
            'logx_ratios': ((lambda x: 1, lambda x: math.log2(x)), ('alogb', 'a')),
            'constant': (lambda x: sum(self.y) / len(self.y), 0, 0, ('const', 's'))
        }
        if the_most_accurate == 'constant':
            self.sheet[the_most_accurate] = tuple([[1], [1]])
        else:
            aproximate_leas_square(base[the_most_accurate])

        return self.Result(self.x, self.y, the_most_accurate, self.sheet)
