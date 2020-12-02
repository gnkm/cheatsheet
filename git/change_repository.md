# Git 管理アカウントとリポジトリ変更手順

プライベートで管理していたリポジトリを仕事用のリポジトリに移行する．
このとき，管理者もプライベートのアカウントから仕事用のアカウントに切り替える．

## bitbucket(移行元のリポジトリホスティングサービス) での操作

bitbucket.org のレポジトリで右上のハンバーガメニューから「リポジトリを共有する」をクリックする．
追加するユーザのメールアドレスを入力，管理者として追加する．
仕事用アカウントで clone する．

## ローカルでの操作

```
git clone git@bitbucket-business:{private-account-name}/xxx.git
```

git ユーザの設定をする．

```
git config --local user.name 'business name'
git config --local user.email 'business mail address'
```

## github での操作

仕事用アカウントで新しい git repository を作成する．

## ローカルでの操作

git remote repository の URL を変更する．

[【git】リポジトリの移行時などでremote urlを変更する - KDE BLOG](https://kde.hateblo.jp/entry/2018/02/18/200459)

```
git remote set-url origin git@github-business:{repository manager name(組織名)}/xxx.git
```

URL が変わっていることを確認する．

```
git remote -v
```

コミット，push する．

```
git commit -m 'something message'
# github ではメインのブランチが master ではなく main になっている
git branch -M main
git  push -u origin master
```
