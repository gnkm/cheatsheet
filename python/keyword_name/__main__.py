import sys

import pac_sample
from pac_sample import subpac_sample


def main():
    print(f'function: {sys._getframe().f_code.co_name}: `__name__`: {__name__}')
    pac_sample.f1()
    pac_sample.f2_from_parent()
    subpac_sample.f2()

    # => function: main: `__name__`: __main__
    # => function: f1: `__name__`: pac_sample
    # => function: f2_from_parent: `__name__`: pac_sample
    # => function: f2: `__name__`: pac_sample.subpac_sample


if __name__ == '__main__':
    main()
