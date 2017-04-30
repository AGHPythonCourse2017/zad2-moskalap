import cmptcomplexity.scripts.parser as prs
import cmptcomplexity.scripts.controller as cntrl
import cmptcomplexity.scripts.task as ctask
import logging
import cmptcomplexity.scripts.strings as ss
import sys
import timeit



def count_it(pattern_invoke,#pattern of invoking code, with __N__ for problem size
          init_code="",#code which make set-up of envoriemnt (__N__ for problem size)
          clean_up_code="",
          timeout=30,
          log_verbose = True):
    if log_verbose:
        if isinstance(log_verbose, str): #logging to file
            logging.basicConfig(filename=log_verbose, level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        else:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(level=logging.WARN, format='%(asctime)s  - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('started program with arguments %s', sys.argv)
    task = ctask.Task(init_code,clean_up_code,example_invoke=pattern_invoke)


    controller = cntrl.Controller(task,30)
    controller.get_data()

    #return controller.get_results()









