import sys

from pac_sample import subpac_sample


def f1():
    print(f'function: {sys._getframe().f_code.co_name}: `__name__`: {__name__}')

def f2_from_parent():
    print(f'function: {sys._getframe().f_code.co_name}: `__name__`: {__name__}')
