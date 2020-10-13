# DataFrame Iteration

## pandas.DataFrame のforループをゆるふわ△改良して300倍高速化する

[pandas.DataFrame のforループをゆるふわ△改良して300倍高速化する - くないらぼ](https://kunai-lab.hatenablog.jp/entry/2018/04/08/134924)

`numpy.ndarray` にする．

```python
import pandas as pd
import timeit


df = pd.DataFrame({"a":list(range(500_000))})
print(df.shape)  # (500000,1)

a = df.a.values
print(type(a))  # numpy.ndarray

def measure():
    for idx in range(df.shape[0]):
        a[idx]

result = timeit.timeit('measure()', globals=globals(), number=1)
```

## Pandas Document

[Essential basic functionality — pandas 1.1.2 documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#iteration)

## python - How to iterate over rows in a DataFrame in Pandas - Stack Overflow

[python - How to iterate over rows in a DataFrame in Pandas - Stack Overflow](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)

### 結論

>  I will concede that there are circumstances where iteration cannot be avoided (for example, some operations where the result depends on the value computed for the previous row). 

`df.iterrows()` を使うしかない．

### 補足

下記方法でできないか調べるべきと回答されている．

1. Vectorization
2. Cython routines
3. List Comprehensions (vanilla for loop)
4. `DataFrame.apply()`
  - i:  Reductions that can be performed in Cython
  - ii: Iteration in Python space
5. `DataFrame.itertuples() and iteritems()
6. `DataFrame.iterrows()
