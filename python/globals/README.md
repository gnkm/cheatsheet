# globals() 関数

```python
class c1:
    def __init__(self):
        pass

    def f1(self, num):
        return num + 1


def f2(x):
    return 2 * x


if __name__ == '__main__':
    c = c1()
    ret_cf1 = c.f1(1)

    print('globals(): {}' .format(globals()))

    # <class 'dict'>
    print('type(globals()): {}'.format(type(globals())))

    # __main__
    print('globals()["__name__"]: {}'.format(globals()['__name__']))

    # 4
    print('globals()["f2"](2): {}'.format(globals()['f2'](2)))

    # 2
    print('c1.f1(1): {}'.format(ret_cf1))
```
