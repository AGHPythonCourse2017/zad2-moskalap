class Solver:
    class Result:
        def __init__(self, x, y, complexity, sheet):
            self.x = x
            self.y = y
            self.complexity_k = complexity
            self.complexity = {
                'linear_ratios' : 'O(N)',
                'square_ratios' : 'O(N^2)',
                'xlogx_ratios' : 'O(N log N)'
,               'logx_ratios'    : 'O(log N)'


            }[complexity]
            self.sheet = sheet
            self.sheet[complexity] = sum(self.sheet[complexity])/len(self.sheet[complexity])


        def show(self):

            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            import numpy as np
            import math

            MAX = self.y[-1]
            xrange = np.linspace(1, self.x[-1], len(self.x))
            logx = list(filter(lambda k: k<=MAX, np.log2(xrange)*self.sheet['logx_ratios']))
            sqr = list(filter(lambda k: k<=MAX,np.power(xrange,2)*self.sheet['square_ratios']))
            xlogx = list(filter(lambda k: k<=MAX,np.log2(xrange)*xrange*self.sheet['xlogx_ratios']))
            linear = list(filter(lambda k: k<=MAX,np.multiply(xrange, self.sheet['linear_ratios'])))



            plt.plot(self.x, self.y, label='results', marker='o', color='r', linestyle='--')
            plt.plot(xrange[0:len(linear)], linear, label='o(N)=', linestyle='--')
            plt.plot(xrange[0:len(logx)], logx, label='o(log N)=', linestyle='--')
            plt.plot(xrange[0:len(xlogx)], xlogx, label='o(N log N)=', linestyle='--')
            plt.plot(xrange[0:len(sqr)], sqr, label='o(N^2)=', linestyle='--')
            plt.legend()
            plt.title(self.complexity)

            plt.xlabel('problem size')
            plt.ylabel('time [cpu ticks]')
            plt.savefig('plot.png')


    def __init__(self,x,y):

        self.points = []
        self.sheet={
            'linear_ratios' : [],
            'square_ratios' : [],
            'xlogx_ratios' : [],
            'logx_ratios'    : [],

        }
        import math

        for i in range(len(x)):
            self.points.append((x[i],y[i]))

        self.x, self.y = map(list, zip(*sorted(self.points, key=lambda k: k[0])))

        for i in range(len(x)):
            self.sheet.get('linear_ratios').append(self.y[i] / self.x[i])
            self.sheet.get('square_ratios').append(self.y[i] / (self.x[i] ** 2))
            self.sheet.get('xlogx_ratios').append(self.y[i]/ (self.x[i] * math.log2(self.x[i])))
            self.sheet.get('logx_ratios').append(self.y[i]/ (math.log2(self.x[i])))




    def solve(self):
        #in sheet there are ratios
        the_most_accurate = None
        diff = 999999
        def count_diff(x):
            avg = sum(x)/len(x)
            diff = 0
            for i in x:
                diff += ((avg-i)/avg)**2
            return diff
        def count_ratio(x):
            return sum(x[1:3])/len(x[1:3])


        for key in self.sheet.keys():
            new_diff = count_diff(self.sheet.get(key))
            if new_diff < diff:
                if the_most_accurate:
                    self.sheet[the_most_accurate]=count_ratio(self.sheet.get(the_most_accurate))

                the_most_accurate=key
                diff = new_diff
            else:
                self.sheet[key] = count_ratio(self.sheet.get(key))

        return self.Result(self.x, self.y,the_most_accurate, self.sheet)




