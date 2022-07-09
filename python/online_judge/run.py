import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sli = lambda: list(map(int, input()))        # input single line int
i_slf = lambda: list(map(float, input()))      # input single line float
i_sls = lambda: list(input())                  # input single line str
i_mli = lambda n: [i_sli() for _ in range(n)]  # input multi line int
i_mlf = lambda n: [i_slf() for _ in range(n)]  # input multi line float
i_mls = lambda n: [i_sls() for _ in range(n)]  # input multi line str

sys.setrecursionlimit(1000000)

def main():
    # python run.py < single_line_float.txt
    # ===== ===== =====
    # a, b, c = input()
    # icecream.ic(a)        # => ic| a: '98.765'
    # icecream.ic(b)        # => ic| b: '43.210'
    # icecream.ic(c)        # => ic| c: '88.65'
    # icecream.ic(type(a))  # => ic| type(a): <class 'str'>

    # python run.py < single_line_float.txt
    # ===== ===== =====
    # a = i_slf()
    # icecream.ic(a)        # => ic| a: [98.765, 43.21, 88.65]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>

    # python run.py < single_line_float.txt
    # ===== ===== =====
    # a, b, c = i_slf()
    # icecream.ic(a)        # => ic| a: 98.765
    # icecream.ic(b)        # => ic| b: 43.21
    # icecream.ic(c)        # => ic| c: 88.65
    # icecream.ic(type(a))  # => ic| type(a): <class 'float'>

    # python run.py < single_line_str.txt
    # ===== ===== =====
    # a, b, c = i_sls()
    # icecream.ic(a)        # => ic| a: 'abcdefghij'
    # icecream.ic(b)        # => ic| b: 'klmnopqrst'
    # icecream.ic(c)        # => ic| c: 'uvwxyx'
    # icecream.ic(type(a))  # => ic| type(a): <class 'str'>

    # python run.py < single_line_float.txt
    # ===== ===== =====
    # a = i_mlf(1)
    # b = a[0]
    # icecream.ic(a)        # => ic| a: [[98.765, 43.21, 88.65]]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>
    # icecream.ic(b)        # => ic| b: [98.765, 43.21, 88.65]
    # icecream.ic(type(b))  # => ic| type(b): <class 'list'>

    # python run.py < multi_line_float.txt
    # ===== ===== =====
    # a = i_mlf(3)
    # icecream.ic(a)        # => ic| a: [[1.123, 2.456, 3.789], [1.456, 2.789, 3.123], [1.789, 2.123, 3.456]]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>

    # python run.py < multi_line_str.txt
    # ===== ===== =====
    # a = i_mls(3)
    # icecream.ic(a)
    # icecream.ic(type(a))
    # <output>
    # ic| a: [['abcdefghij', 'klmnopqrst', 'uvwxyx'],
    #         ['klmnopqrst', 'abcdefghij', 'uvwxyx'],
    #         ['uvwxyx', 'abcdefghij', 'klmnopqrst']]
    # ic| type(a): <class 'list'>

    # python run.py < first_int_second_float.txt
    # ===== ===== =====
    # a = i_sli()
    # b = i_mlf(a[0])
    # icecream.ic(a)        # => ic| a: [3]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>
    # icecream.ic(b)        # => ic| b: [[1.123, 2.456, 3.789], [1.456, 2.789, 3.123], [1.789, 2.123, 3.456]]
    # icecream.ic(type(b))  # => ic| type(b): <class 'list'>


if __name__ == '__main__':
    main()
