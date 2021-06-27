# GitHub

## Issue とカンバンの連携

- Project で automated kanban を作る
- Todo 列の 3 点ドットをクリックし Manage automation を選択する
- 設定する
- Issue 作成時に，右にある Projects をクリックし，任意のリポジトリを選択する

## ローカルに main ブランチを作らない

cf. [gitでローカルブランチにmasterなんて（普通は）要りません - Qiita](https://qiita.com/igrep/items/f2e927a31e826766b8c0)

```
git config --global push.default current
git checkout -b feature1 origin/master

# origin/master に対してrebaseできる
git pull --rebase

# push先はリモートの同名ブランチである origin/feature1 になる
git push
