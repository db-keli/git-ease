#!/usr/bin/env python3

from wizard import squash
import re
import sys


args = sys.argv

# Add one file and commit/commit and push 

# When there's only -f argument(add and commit only)

if args[1] == '-f' and args[2] != '-p':
    index = args.index('-f')
    squash.addFileAndCommit(args, index)

# When arguments begin with -f -p
elif args[1] == '-f' and args[2] == '-p':
    index = args.index('-p')
    squash.addFileAndCommit(args, index)
    squash.push()

# When arguments begin with -fp or -pf(add, commit and push)   
elif (re.search('-fp', arg) for arg in args) or (re.search('pf', arg) for arg in args):
    for arg in args:
        match1 = re.findall('-fp', arg)
        match2 = re.findall('-pf', arg)
    
    if match1:
        index1= args.index('-pf')
        squash.addFileAndCommit(args, index1)
        squash.push()
    elif match2:
        index2 = args.index('-fp')
        squash.addFileAndCommit(args, index2)
        squash.push()
        

# Add all files and commit/commit and push

# When arguments begin with -a only(add and commit only)
if args[1] == '-a':
    index = args.index('-a')
    squash.addAllAndCommit(args, index)

# When arguments begin with -a -p(add, commit and push them)
elif args[1] == '-a' and args[2] == '-p':
    index = args.index('-p')
    squash.addAllAndCommit(args, index)
    squash.push()

# When arguments begin with -ap or -pa(add, commit and push files)
elif (re.search('-ap', arg) for arg in args) or (re.search('-pa', arg) for arg in args):
    for arg in args:
        match1 = re.findall('-ap', arg)
        match2 = re.findall('-pa', arg)

    if match1 is not None:
        try:
            index1= args.index('-ap')
            squash.addAllAndCommit(args, index1)
            squash.push()
            print("shit worked")
        except ValueError:
            pass

    if match2 is not None:
        try:
            index2 = args.index('-pa')
            squash.addAllAndCommit(args, index2)
            squash.push()
            print("Shit worked")
        except ValueError:
            pass
