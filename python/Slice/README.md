# Slice

下記リストを扱う．

```
_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## リストの値を取り出す

```
print(_list[1]) # => 1
print(_list[9]) # => 9, 境界値
print(_list[-1]) # => 9
print(_list[-10]) # => 0, 境界値
```

## スライス

### 使い方

```
_list[start_index:end_index + 1:step_num]
```

ただし，返り値に含まれるのは `_list[end_index]` まで．

### step_num なし

```
print(_list[:]) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(_list[0:10]) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(_list[3:]) # => [3, 4, 5, 6, 7, 8, 9]
print(_list[:5]) # => [0, 1, 2, 3, 4]

print(_list[3:6]) # => [3, 4, 5]
print(_list[6:3]) # => []

print(_list[:-1]) # => [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

start_num < 0 の場合，返り値に含まれるのは `_list[start_num + 1]` から

```
print(_list[-3:]) # => [7, 8, 9]
print(_list[-2:-1]) # => [8]
print(_list[-10:-2]) # => [0, 1, 2, 3, 4, 5, 6, 7]
```

### step_num あり

```
print(_list[0:10:1]) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(_list[::2]) # => [0, 2, 4, 6, 8]
print(_list[::-1]) # =>[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(_list[3:6:-1]) # =>[]
print(_list[6:3:-1]) # =>[6, 5, 4]
print(_list[-5:-9:-1]) # =>[5, 4, 3, 2]
```
