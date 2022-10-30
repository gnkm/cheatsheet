# Currying

## Background

I tried to organize currying.
I use the following haskell code.

```haskell
sum3 :: (Num a) => a -> a -> a -> a
sum3 x y z = x + y + z
```

## Create virtual env

```
anyenv install pyenv
pyenv install 3.10.1
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.10.1/bin/python
```

### Prepare

```
poetry shell
poetry install
```

### Execute

```
python __main__.py
```
