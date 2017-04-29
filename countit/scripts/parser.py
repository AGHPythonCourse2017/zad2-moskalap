import argparse
from argparse import RawTextHelpFormatter


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
        self.parser.add_argument('-i','--init',
                                 help='specify a initialization part (string or *.py file)\n\n',
                                 default=None)
        self.parser.add_argument('invoke_example',
                                 help='specify a pattern to invoke a method/function\n'
                                      'where "_N_" is parameter responsilbe for problem size\n'

                                      'example:\t "object.method_to_test(arg1, arg2, _N_, arg4)"\n\n')
        self.parser.add_argument('-c', '--clean',
                                 help='specify a clea-up code (string or *.py file)\n\n',
                                 default=None)
        self.parser.add_argument('-t','--timeout',
                                 help='Timeout for algorithm in seconds, default 30',
                                 default=30.0,
                                 type=float)
        self.args = self.parser.parse_args()

