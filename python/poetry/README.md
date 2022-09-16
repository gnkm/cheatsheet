# Poetry

## Usage

### Create virtual env

Install `pyenv`.

```
anyenv install pyenv
```

Install any version.

```
pyenv install 3.10.1
```

Specify the version to use.

```
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.10.1/bin/python
```

Enter virtual environment.

```
poetry shell
```

### Preparation

make `pyproject.toml`.

```toml
[tool.poetry]
name = "something_package"
version = "0.1.0"
description = ""
authors = ["gnkm <genki.matsunaga@gmail.com>"]

[tool.poetry.dependencies]
python = "3.10.1"

[tool.poetry.dev-dependencies]
icecream = "^2.1.2"
flake8 = "^4.0.1"
pylint = "^2.14.1"
pytest = "^7.1.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

install packages.

```
poetry install
```

### Execute

```
python xxx.py
```

### Exit virtual env

```
exit
```
