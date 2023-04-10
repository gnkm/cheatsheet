# Manipulate Audio Files

## Convert File

Use `ffmpeg` command.

```sh
ffmpeg -i input.m4a output.wav
```

You can `afconvert` command if you use Mac.

```sh
afconvert -f WAVE -d LEI16 input.m4a output.wav
```

## Split File

```sh
sox input.wav output.wav trim 0 3600 : newfile : restart
```

## Change Speed

```sh
sox input.wav output.wav speed 1.25
```

## Reference

- [SoX Documentation](https://sox.sourceforge.net/sox.html)
- [ffmpeg Documentation](https://ffmpeg.org/documentation.html)
