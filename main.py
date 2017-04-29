import countit.scripts.parser as prs
import countit.scripts.controller as cntrl
import logging
import countit.scripts.strings as ss
import sys

logging.basicConfig(filename=ss.Strings.LOGS,level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('started program with arguments %s', sys.argv)
p = prs.Parser()

controller = cntrl.Controller(p)

for i in range(0,6):
    f = controller.run(i)
    f()
    print(a)

#exec("funkcja(1,2)")
#abst_fun(1,"ad")
#exec()
#print(a)






