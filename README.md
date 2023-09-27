# 🪄 gitWiz
gitWiz is simply an automation script that makes life with git easier.

### The Idea ?
When working on a project with a bunch of files, staging, commit and pushing files could be time wasting sometimes, especially
when you want to commit some files, push some files or just stage some files at a point. With gitWiz, you do this at a go!
<!-- gitWiz will also keep records of what you do. gitWiz presents a more easy to read log that will show when(exact day and time) you added, committed or pushed and
the files you did that to. -->
Looking to make adding, commiting, pushing and time traveling in git so easy when working with a lot of tasks.
Still working on making the use of git as simple as possible!

Usage
===========
gwiz [options]pattern-spec [files]pattern-spec [commit message]

Options
===========
*-a*<br>
Add all files and commit them<br>
```
gwiz -a [commit message]
```
*-f*<br>
Add a single file and commit<br>
```
gwiz -f [filename] [commit message]
```
*-p*<br>
In conjuction with -a or -f to push<br>
```
gwiz -f -p [filename] [commit message]
gwiz -a -p [commit message]
```
Install
=======
Clone this repository and execute the install.sh file <br>
```
./install.sh
```


