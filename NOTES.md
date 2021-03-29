## Pushing to Github on Linux:
if adding a new file:
```
git add -a
```
else:
```
git commit -a
git push
```

## Notes on linux terminal:
Rename Directory:
```
mv dir1 dir2
```
Delete Directory:
```
rm -r <directory name>
```

Edit a file:
```
sudo nano <filename>
```

Make a directory:
```
mkdir <directory name>
```

Make a new file:
```
touch <filename>
```

Navigate to previous directory:
```
cd -
```
## Store Sign-in info with git:
```
$ git config credential.helper store
$ git push https://github.com/owner/repo.git

Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD>
```