# Ignore files recursively

```
path1/path2/*
!path1/path2/.gitkeep
!path1/path2/path3/
path1/path2/path3/*
!path1/path2/path3/.gitkeep
!path1/path2/path3/path4
path1/path2/path3/path4/*
!path1/path2/path3/path4/.gitkeep
```

Then, git manage the following files.

```
git ls path1/path2/
path1/path2/.gitkeep
path1/path2/path3/.gitkeep
path1/path2/path3/path4/.gitkeep
```
