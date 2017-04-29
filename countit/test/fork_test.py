import os
import time
i = 0
k = 0
while i < 5:
    i+=1
    k = [5,4,3,2,1]
    newpid = os.fork()
    if newpid == 0:
        k.append(0)
        time.sleep(2)
        print('<c>')
        print(k)
        print('</c>\n')

    else:
        os.wait()
        print('<p>')
        print(k)
        print('</p>\n')
