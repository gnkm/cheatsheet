# ローカルに main ブランチを作らない

cf. [gitでローカルブランチにmasterなんて（普通は）要りません - Qiita](https://qiita.com/igrep/items/f2e927a31e826766b8c0)

```
git config --global push.default current
```

※ これは `.gitconfig` に下記を追加するのと同じ

```
[push]
	default = current
```

```
git checkout -b feature1 origin/master

# origin/master に対してrebaseできる
git pull --rebase

# push先はリモートの同名ブランチである origin/feature1 になる
git push

git branch --delete master
```
