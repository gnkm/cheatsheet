# github 複数アカウント運用

## 仕事用 ssh 鍵を作成する

プライベート用に '.ssh/id_rsa.pub', '.ssh/id_ecdsa.pub' が存在するものとする。

```
cd $HOME
ssh-keygen -t rsa -b 4096 -f .ssh/id_rsa_business -C {mail@example.com}
ssh-keygen -t ecdsa -b 384 -f .ssh/id_ecdsa_business  -C {mail@example.com}
```

## .ssh/config を編集する

```
Host github-private
  HostName github.com
  User {private user name}
  Port 22
  IdentityFile ~/.ssh/id_ecdsa
  PasswordAuthentication no
# 仕事用アカウント情報を追加する
Host github-business
  HostName github.com
  User {business user name}
  Port 22
  IdentityFile ~/.ssh/id_ecdsa_business
  PasswordAuthentication no
```

## github に公開鍵を登録する

アイコン > Settings > SSH and GPG keys で登録する。

## 接続を確認する

```
ssh -T git@github-business
```

接続できれば下記のように表示される。

```
Hi {yourname}! You've successfully authenticated, but GitHub does not provide shell access.
```

## レポジトリを取得する

### レポジトリを folk する

GitHub のレポジトリページにある「Folk」ボタンをクリックする。

### レポジトリを clone する

Github でコピーできる URL 

`git@github.com:{business user name}/{repository name}.git`

にある `github.com` の部分を `github-business` に変更した

`git@github-business:{business user name}/{repository name}.git`

で clone する。

```
git clone git@github-business:genki-matsunaga/{repository name}.git
```

### コミットするユーザーのアカウントを編集する

```
cd my/project
git config --local user.name "サブアカウント"
git config --local user.email "サブアカウントメールアドレス"
```
