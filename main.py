import countit.scripts.parser as prs
import countit.scripts.controller as cntrl
import logging
import countit.scripts.strings as ss
import sys

logging.basicConfig(filename=ss.Strings.LOGS,level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('started program with arguments %s', sys.argv)
p = prs.Parser()

controller = cntrl.Controller(p)

with open('./countit/temporary_files/init.py', 'r') as content_file:
    content = content_file.read()
exec(content)
j = controller.run()
b = Test(2)
j()
#exec()
#print(a)






