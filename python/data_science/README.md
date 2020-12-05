# Data Science Cheat Sheet

## DataFrame

```python
data = {
    'col1': ['a', 'a', 'b', 'b', 'c', 'c'],
    'col2': [10, 20, 30, 40, 50, 60],
    'col3': [11, 22, 33, 44, 55, 66],
}
_df = pd.DataFrame(data)
_df
```

|   |col1|col2|col3|
|---|----|----|----|
|  0|   a|  10|  11|
|  1|   a|  20|  22|
|  2|   b|  30|  33|
|  3|   b|  40|  44|
|  4|   c|  50|  55|
|  5|   c|  60|  66|

## Datetime

```
df['date'] = df['datetime'].dt.date
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['day_of_week'] = df['datetime'].dt.dow
```

## Preprocessing

```
train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# Now drop the  'Id' colum since it's unnecessary for  the prediction process.
train.drop("Id", axis = 1, inplace = True)
test.drop("Id", axis = 1, inplace = True)

ntrain = train.shape[0]
ntest = test.shape[0]
y_train = train['target_var'].values
all_data = pd.concat((train, test)).reset_index(drop=True)
all_data.drop(['target_var'], axis=1, inplace=True)

# Preprocessing
all_data['feature'] = all_data.apply(preprocessor, axis='columns')

train = all_data[:ntrain]
test = all_data[ntrain:]
```

## groupby().agg()

```python
data = {
    'col1': ['a', 'a', 'b', 'b', 'c', 'c'],
    'col2': [10, 20, 30, 40, 50, 60],
    'col3': [11, 22, 33, 44, 55, 66],
}
_df = pd.DataFrame(data)
_df
```

|   |col1|col2|col3|
|---|----|----|----|
|  0|   a|  10|  11|
|  1|   a|  20|  22|
|  2|   b|  30|  33|
|  3|   b|  40|  44|
|  4|   c|  50|  55|
|  5|   c|  60|  66|

```
_df.groupby('col1', as_index=False).agg('sum')
```

|   |col1|col2|col3|
|---|----|----|----|
|  0|   a|  30|  33|
|  1|   a|  70|  77|
|  2|   b| 110| 121|

```python
def _my_sum(s):
    return s.sum()

_df.groupby('col1', as_index=False).agg(_my_sum)
```

|   |col1|col2|col3|
|---|----|----|----|
|  0|   a|  30|  33|
|  1|   a|  70|  77|
|  2|   b| 110| 121|

## groupby().apply()


```python
data = {
    'col1': ['a', 'a', 'b', 'b', 'c', 'c'],
    'col2': [10, 20, 30, 40, 50, 60],
    'col3': [11, 22, 33, 44, 55, 66],
}
_df = pd.DataFrame(data)
_df
```

|   |col1|col2|col3|
|---|----|----|----|
|  0|   a|  10|  11|
|  1|   a|  20|  22|
|  2|   b|  30|  33|
|  3|   b|  40|  44|
|  4|   c|  50|  55|
|  5|   c|  60|  66|

`groupby()` なしの場合

```python
def _my_sum(r):
    return r['col2'] + r['col3']

_df.apply(_my_sum, axis='columns')
```

|||
|--|--|
| 0|   21|
| 1|   42|
| 2|   63|
| 3|   84|
| 4|  105|
| 5|  126|

`groupby()` ありの場合

```python
def _my_sum(r):
    return (r['col2'] + r['col3']).sum()

_df.groupby('col1', as_index=False).apply(_my_sum)
```

|col1|NaN|
|--|--|
| 0|   63|
| 1|  147|
| 2|  231|

col1 の各値に対して、r2_score() を求めたい

```python
_df_a = _df.query('col1 == "a"')
score = r2_score(_df_a['col2'], _df_a['col3'])
print(f'a: {score:.2f}')

_df_b = _df.query('col1 == "b"')
score = r2_score(_df_b['col2'], _df_b['col3'])
print(f'b: {score:.2f}')

_df_c = _df.query('col1 == "c"')
score = r2_score(_df_c['col2'], _df_c['col3'])
print(f'c: {score:.2f}')
```

a: 0.90
b: 0.50
c: -0.22

```python
def _my_r2_score(r):
    return r2_score(r['col2'], r['col3'])

_df.groupby('col1').apply(_my_r2_score)
```

|col1||
|--|--|
| a|  0.90|
| b|  0.50|
| c| -0.22|
