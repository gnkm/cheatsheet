import sys


def f2():
    print(f'function: {sys._getframe().f_code.co_name}: `__name__`: {__name__}')
