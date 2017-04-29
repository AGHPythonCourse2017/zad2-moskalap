import os
#os.system("/home/przemek/Dokumenty/Projects/applications/python/zad2/zad2-moskalap/time_saver.sh")

with open("/home/przemek/Dokumenty/Projects/applications/python/zad2/zad2-moskalap/test/wyniki.txt") as f:
    content = f.readlines()

print("ok")
x=[]
y=[]
liny=[]
quy=[]
logy = []
a_lin =[]
a_x2 =[]
a_log =[]
import matplotlib.pyplot as plt
def convert(a):
    if a == 'usec':
        return 1
    if a == 'msec':
        return 1000
    return 1000000

import math

for line in content:
    print(line)
    line = line.split()
    act_x = float(line[0])
    act_y = float(line[1])*convert(line[2])
    x.append(act_x)
    y.append(act_y)
    a_lin.append(act_y / act_x)
    a_x2.append(act_y/(act_x**2))
    a_log.append(act_y/(act_x*math.log2(act_x)))

a_ratio= sum(a_lin)/len(a_lin)
ax2_ratio = sum(a_x2)/len(a_x2)
alog = sum(a_log)/len(a_log)

for act_x in x:
    quy.append(ax2_ratio*(act_x**2))
    liny.append(act_x)
    logy.append(math.log2(act_x)*act_x)

print(x)
print(y)
print(quy)
plt.plot(x,y,x,liny,x, logy)
plt.show()

