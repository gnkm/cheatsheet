# Git CheetSheet

## Squash some commits

Check commits.

```
git log --oneline
```

Run `git rebase` command.

```
git rebase -i $ {commit hash}
```

Following display appears.
Top commit is the oldest.

```
pick 555582c Add an algorithm for accessing new tab page
pick 78764f9  Modify gettime()
pick 62419f2 Delete unnecessary comment
```

Squash 62419f2 to 555582c.
Edit text like following.

```
pick 555582c Add an algorithm for accessing new tab page
squash 62419f2 Delete unnecessary comment
pick 78764f9  Modify gettime()
```

Save(`:wq`).
Following display appears.

```
# This is a combination of 2 commits.
# The first commit's message is:

Add an algorithm for accessing new tab page

# This is the 2nd commit message:

Delete unnecessary comment
```

Edit message.

```
Add an algorithm for accessing new tab page
and delete unnecessary comment

# This is a combination of 2 commits.
# The first commit's message is:

Add an algorithm for accessing new tab page

# This is the 2nd commit message:

Delete unnecessary comment
```

Save(`:wq`).
