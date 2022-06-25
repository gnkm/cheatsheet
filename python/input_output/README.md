# Input and Output

## Usage

First, edit `__main__.py`, and executes.

single element

```
python __main__.py < single_element_str.txt
python __main__.py < single_element_int.txt
python __main__.py < single_element_float.txt
```

single line

```
python __main__.py < single_line_str.txt
python __main__.py < single_line_int.txt
python __main__.py < single_line_float.txt
```

multi line

```
python __main__.py < multi_line_str.txt
python __main__.py < multi_line_int.txt
python __main__.py < multi_line_float.txt
```

## code

`__main__.py`

```python
from pprint import pprint
import sys


def main():
    # ===== single element =====
    # ret = int(input()) 
    # ret = float(input())
    # ret = input()  # string
    # pprint(ret)

    # ===== single line =====
    # aaa, bbb, ccc = input().split()
    # aaa, bbb, ccc = map(int, input().split())
    # aaa, bbb, ccc = map(float, input().split())
    # pprint(aaa, bbb, ccc)

    # ===== single line to list =====
    # ret = input().split()
    # ret = list(map(int, input().split()))
    # ret = list(map(float, input().split()))
    # pprint(ret)

    # ===== multi line =====
    N = 3
    type_ = str  # int, float, or str
    ret = [list(map(type_, input().split())) for _ in range(N)]
    pprint(ret)

    sys.exit(0)


if __name__ == '__main__':
    main()

```

## inputs

### single element

`single_element_str.txt`

```
abcdefg
```

`single_element_int.txt`

```
123
```

`single_element_float.txt`

```
98.765
```

`single_line_str.txt`

```
abcdefghij klmnopqrst uvwxyx
```

`single_line_int.txt`

```
123 456 789
```

`single_line_float.txt`

```
98.765 43.210 88.65
```

`multi_line_str.txt`

```
abcdefghij klmnopqrst uvwxyx
klmnopqrst abcdefghij uvwxyx
uvwxyx abcdefghij klmnopqrst
```

`multi_line_int.txt`

```
123 456 789
456 789 123
789 123 456
```

`multi_line_float.txt`

```
1.123 2.456 3.789
1.456 2.789 3.123
1.789 2.123 3.456
```
