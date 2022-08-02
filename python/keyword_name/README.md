# Check keyword `__name__`

## Background

When logging, it is generally written as `logger = logging.getLogger(__name__)`. I check `__name__` in it.

## Create virtual env

```
anyenv install pyenv
pyenv install 3.8.13
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.8.13/bin/python
```

### Prepare

```
poetry install
poetry shell
```

### Execute

```
python __main__.py
```
