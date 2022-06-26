# About `!!`, `$_`, `!$` in fish

You can use `!!`, `$_`, `!$` in fish after installing `oh-my-fish/plugin-bang-bang`.

```
fisher install oh-my-fish/plugin-bang-bang
```

cf. [oh-my-fish/plugin-bang-bang](https://github.com/oh-my-fish/plugin-bang-bang)

You can use the function by adding the following to the `config.fish`.

```
if [ -f $HOME/.config/fish/functions/__history_previous_command.fish ]; source $HOME/.config/fish/functions/__history_previous_command.fish; end
if [ -f $HOME/.config/fish/functions/__history_previous_command_arguments.fish ]; source $HOME/.config/fish/functions/__history_previous_command_arguments.fish; end
if [ -f $HOME/.config/fish/conf.d/plugin-bang-bang.fish ]; source $HOME/.config/fish/conf.d/plugin-bang-bang.fish; end
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

```
echo foo bar
echo !$
# => bar
```
