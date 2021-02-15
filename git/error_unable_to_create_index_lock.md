# fatal: Unable to create 'path/to/repository/.git/index.lock': File exists.

```
git restore file
```

の後、下記メッセージが表示された。

```
fatal: Unable to create 'path/to/repository/.git/index.lock': File exists.

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.
```

## やったこと

### `ls`

.git/index.lock はない。

### .git/COMMIT_EDITMSG 削除

```
mv .git/COMMIT_EDITMSG $HOME/Documents
```

の後、下記コマンドを実行。

```
git restore file
```

成功した。
