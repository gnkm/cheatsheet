# About `!!`, `$_`, `!$` in fish

You can use `!!`, `$_`, `!$` in fish after installing `oh-my-fish/plugin-bang-bang`.

```
fisher install oh-my-fish/plugin-bang-bang
```

## Examples

```
echo foo bar
# => foo bar
```

```
# alt + . => bar
# alt + s => sudo echo
```

```
echo foo bar
echo !!
# When input `!!`, expanded "echo echo foo bar" 
# => echo foo bar
```

```
echo foo bar
echo $_
# => echo
```
