import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                    # input single element single line int
i_seslf = lambda: float(input()[0])                  # input single element single line float
i_sesls = lambda: str(input()[0])                    # input single element single line str
i_semli = lambda n: [i_sesli() for _ in range(n)]    # input single element multi line int
i_semlf = lambda n: [i_seslf() for _ in range(n)]    # input single element multi line float
i_semls = lambda n: [i_sesls() for _ in range(n)]    # input single element multi line str
i_mesli = lambda: list(map(int, input()))            # input multi element single line int
i_meslf = lambda: list(map(float, input()))          # input multi element single line float
i_mesls = lambda: list(input())                      # input multi element single line str
i_memli = lambda n: [i_mesli() for _ in range(n)]    # input multi element multi line int
i_memlf = lambda n: [i_meslf() for _ in range(n)]    # input multi element multi line float
i_memls = lambda n: [i_mesls() for _ in range(n)]    # input multi element multi line str

sys.setrecursionlimit(1000000)

def main():
    # python run.py < single_element_single_line_float.txt
    # ===== ===== =====
    # a = i_seslf()
    # icecream.ic(a)        # => ic| a: 98.765
    # icecream.ic(type(a))  # => ic| type(a): <class 'float'>

    # python run.py < single_element_multi_line_float.txt
    # ===== ===== =====
    # a = i_semlf(3)
    # icecream.ic(a)        # => ic| a: [1.123, 1.456, 1.789]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>

    # python run.py < multi_element_single_line_float.txt
    # ===== ===== =====
    # a, b, c = input()
    # icecream.ic(a)        # => ic| a: '98.765'
    # icecream.ic(b)        # => ic| b: '43.210'
    # icecream.ic(c)        # => ic| c: '88.65'
    # icecream.ic(type(a))  # => ic| type(a): <class 'str'>

    # python run.py < multi_element_single_line_float.txt
    # ===== ===== =====
    # a = i_meslf()
    # icecream.ic(a)        # => ic| a: [98.765, 43.21, 88.65]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>

    # python run.py < multi_element_single_line_float.txt
    # ===== ===== =====
    # a, b, c = i_meslf()
    # icecream.ic(a)        # => ic| a: 98.765
    # icecream.ic(b)        # => ic| b: 43.21
    # icecream.ic(c)        # => ic| c: 88.65
    # icecream.ic(type(a))  # => ic| type(a): <class 'float'>

    # python run.py < multi_element_single_line_str.txt
    # ===== ===== =====
    # a, b, c = i_mesls()
    # icecream.ic(a)        # => ic| a: 'abcdefghij'
    # icecream.ic(b)        # => ic| b: 'klmnopqrst'
    # icecream.ic(c)        # => ic| c: 'uvwxyx'
    # icecream.ic(type(a))  # => ic| type(a): <class 'str'>

    # python run.py < multi_element_single_line_float.txt
    # ===== ===== =====
    # a = i_memlf(1)
    # b = a[0]
    # icecream.ic(a)        # => ic| a: [[98.765, 43.21, 88.65]]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>
    # icecream.ic(b)        # => ic| b: [98.765, 43.21, 88.65]
    # icecream.ic(type(b))  # => ic| type(b): <class 'list'>

    # python run.py < multi_element_multi_line_float.txt
    # ===== ===== =====
    # a = i_memlf(3)
    # icecream.ic(a)        # => ic| a: [[1.123, 2.456, 3.789], [1.456, 2.789, 3.123], [1.789, 2.123, 3.456]]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>

    # python run.py < multi_element_multi_line_str.txt
    # ===== ===== =====
    # a = i_memls(3)
    # icecream.ic(a)
    # icecream.ic(type(a))
    # <output>
    # ic| a: [['abcdefghij', 'klmnopqrst', 'uvwxyx'],
    #         ['klmnopqrst', 'abcdefghij', 'uvwxyx'],
    #         ['uvwxyx', 'abcdefghij', 'klmnopqrst']]
    # ic| type(a): <class 'list'>

    # python run.py < first_int_second_float.txt
    # ===== ===== =====
    # a = i_sesli()
    # b = i_memlf(a)
    # icecream.ic(a)        # => ic| a: [3]
    # icecream.ic(type(a))  # => ic| type(a): <class 'list'>
    # icecream.ic(b)        # => ic| b: [[1.123, 2.456, 3.789], [1.456, 2.789, 3.123], [1.789, 2.123, 3.456]]
    # icecream.ic(type(b))  # => ic| type(b): <class 'list'>

    sys.exit()


if __name__ == '__main__':
    main()
