# ローカルに main ブランチを作らない

cf. [gitでローカルブランチにmasterなんて（普通は）要りません - Qiita](https://qiita.com/igrep/items/f2e927a31e826766b8c0)

`git push` でプッシュするブランチを指定せずにすむようにする。
(現在のブランチをプッシュする。)

```
git config --global push.default current
```

※ これは `.gitconfig` に下記を追加するのと同じ

```
[push]
	default = current
```

ブランチ作成

```
git checkout -b feature1 origin/main
```

origin/main に対してrebase する。

```
git pull --rebase
```

この時 push 先はローカルの同名ブランチである origin/feature1 になる

```
git push
```

ローカルの main ブランチを削除する。

```
git branch --delete main
```
