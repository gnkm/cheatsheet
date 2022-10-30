"""
Haskell における下記 `sum3` がカリー化されて実行される方法を Python で表現する。
sum3 :: (Num a) => a -> a -> a -> a
sum3 x y z = x + y + z

-- sum3 は下記のシンタックスシュガー
sum3Lambda :: (Num a) => a -> a -> a -> a
sum3Lambda = \\x -> (\\y -> (\\z -> x + y + z))

※ バックスラッシュ 2 つであることについて
Python では docstring の中でバックスラッシュ 1 つ使うとシンタックスエラーになるので
バックスラッシュ 2 つが Haskell におけるバックスラッシュ 1 つであるものとして表現した
"""

from functools import partial
from typing import Callable


def main():
    x = 1
    y = 2
    z = 3

    val_simple = sum3_simple(x, y, z)
    val_curry = sum3_curry(x, y, z)
    val_lambda = (
        lambda _x: (
            lambda _y: (
                lambda _z: _x + _y + _z
            )
        )
    )(x)(y)(z)

    # 部分適用
    sum3_x = partial(sum3_simple, x)
    sum3_x_y = partial(sum3_x, y)
    val_partial = sum3_x_y(z)

    print(f'{val_simple = }')  # => 6
    print(f'{val_curry = }')  # => 6
    print(f'{val_lambda = }')  # => 6
    print(f'{val_partial = }')  # => 6


def sum3_simple(x: int, y: int, z: int) -> int:
    return x + y + z


def sum3_curry(x: int, y: int, z: int) -> int:
    """Return x + y + z.

    カリー化して算出する。

    大まかに書くと下記のとおり。

    sum3_curry(x, y, z) = f(x)(y)(z) = g(y)(z) = h(z) = x + y + z

    h(z) が本質の関数。
    カリー化なので内部の関数は引数を 1 つしかとらず、コードで書くと h(z) となるが
    x, y が使えるスコープなので、実質は(数学的に表現すると) h(x, y, z) である。
    h(z) 内では x, y が固定されているため、関数定義では z のみを引数にとることになる。

    Args:
        x (int): _description_
        y (int): _description_
        z (int): _description_

    Returns:
        int: x + y + z
    """
    def f(_x: int) -> Callable:
        """f

        Args:
            _x (int): _description_

        Returns:
            Callable: g  s.t. g(y: int) -> Callable
        """
        def g(_y: int) -> Callable:
            """g

            Args:
                _y (int): _description_

            Returns:
                Callable: h  s.t. h(z: int) -> int
            """
            def h(_z: int) -> int:
                """本質の関数"""
                return _x + _y + _z

            return h

        return g

    return f(x)(y)(z)


if __name__ == '__main__':
    main()
