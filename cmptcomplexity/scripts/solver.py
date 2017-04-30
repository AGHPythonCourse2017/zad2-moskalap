class Solver:
    class Result:
        def __init__(self, x, y, complexity, how_long=None, how_many=None):
            self.x = x
            self.y = y
            self.complexity = complexity
            self.how_long = how_long
            self.how_many = how_many


    def __init__(self,x,y):

        self.points = []
        self.liny = []
        self.quy = []
        self.logy = []
        self.a_lin = []
        self.a_x2 = []
        self.a_log = []
        import math

        for i in range(len(x)):
            self.points.append((x[i],y[i]))

        self.x, self.y = map(list, zip(*sorted(self.points, key=lambda k: k[0])))

        for i in range(len(x)):
            self.a_lin.append(self.y[i] / self.x[i])
            self.a_x2.append(self.y[i] / (self.x[i] ** 2))
            self.a_log.append(self.y[i]/ (self.x[i] * math.log2(x[i])))

        self.sheet={

        }
        self.a_ratio = sum(self.a_lin[0:10]) / len(self.a_lin[0:10])
        self.ax2_ratio = sum(self.a_x2) / len(self.a_x2)

        self.alog = self.a_log[10]
        self.ref_x = []
        for act_x in range(10,self.x[-1]):
            self.ref_x.append(act_x)
            self.quy.append(self.ax2_ratio * (act_x ** 2))
            self.liny.append(self.a_ratio* act_x)
            self.logy.append(self.alog*math.log2(act_x) * act_x)
        self.solve()


    def solve(self):
        import matplotlib.pyplot as plt
        import numpy as np


        print('x', self.x)
        print('y', self.y)
        print('x^2', self.quy)
        print('x', self.liny)
        print('xlogx', self.logy)
        q = [(x - y) ** 2 for x, y in zip(self.y, self.quy)]
        print('y/x^2', sum(q) / len(q), q)
        l = [(x - y) ** 2 for x, y in zip(self.y, self.liny)]
        print('y/x', sum(l) / len(l), l)
        lg = [(x - y) ** 2 for x, y in zip(self.y, self.logy)]
        print('y/xlogx', sum(lg) / len(lg), lg)
        plt.plot(self.x, self.y, label='results', marker='o', color='r', linestyle='--')
        plt.plot(self.ref_x, self.liny, label='teor_lin', linestyle='--')
        plt.plot(self.ref_x, self.logy, label='teor_nlogn', linestyle='--')
        self.max = self.y[-1]

        self.quy = list(filter(lambda k: k < self.max, self.quy))
        plt.plot(self.ref_x[:len(self.quy)], self.quy[:len(self.quy)], label='teor n^2', linestyle='--')
        plt.legend()

        plt.xlabel('problem size')
        plt.ylabel('time [cpu ticks]')
        plt.show()
