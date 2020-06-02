# Pipenv Cheetsheet

## Reference

[Pipenv: Python Dev Workflow for Humans](https://pipenv.readthedocs.io/en/latest/)

## Usage

### Starting project

#### Specifying Versions of Python

```
$ cd myproject
# list versions be able to use
$ pyenv install --list
$ pyenv install 3.6
$ pipenv --python 3.6
```

If you have not installed ver 3.6, it install ver3.6.  
This command generates `Pipfile`.

### After cloning

```
$ cd myproject
$ pipenv install
```

### Environment Management with Pipenv

```
$ pipenv install [package names]
```

#### Make Pipfile.lock

After installing some packages, you should make `Pipfile.lock` with following command.

```
$ pipenv lock
```

## Execute

```
$ pipenv run python something.py
```

### Alias

When you edit `Pipfile` like following, you can execute the script with `pipenv run something`.

```
[scripts]

something = "python something.py"
```

