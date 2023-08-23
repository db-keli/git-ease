git-squash-0.0.1
===============

Version 0.0.1 <br>

# squash

Usage
===========
squash [options ...]pattern-spec [files ...]pattern-spec [commit message ... ]

Purpose
===========
To simplify git commands

Options
===========
*-a*<br>
Add all files and commit them<br>
```
squash -a [commit message]
```
*-f*<br>
Add a single file and commit<br>
```
squash -f [filename] [commit message]
```
*-p*<br>
In conjuction with -a or -f to push<br>
```
squash -f -p [filename] [commit message]
squash -a -p [commit message]
```
Install
=======
Clone this repository and execute the install.sh file <br> as a root user.<br>
```
sudo ./install.sh
```
