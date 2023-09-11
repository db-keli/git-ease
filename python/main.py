#!/usr/bin/env python3

from Squasher.squash import *
import re
import sys
import subprocess


args = sys.argv

if args[1] == '-f' and args[2] != '-p':
    index = args.index('-f')
    addFileAndCommit(args, index)

elif args[1] == '-a' and args[2] != '-p':
    index = args.index('-a')
    addAllAndCommit(args, index)

elif (re.search('-fp', arg) for arg in args) or (re.search('pf', arg) for arg in args):
    for arg in args:
        match1 = re.findall('-fp', arg)
        match2 = re.findall('-pf', arg)
        print(f"This is {match1} and this is {match2}")
    
    if match1 != None or match2 != None:
        index1 = args.index('-pf')
        # index2 = args.index('fp')
        if index1:
            addFileAndCommit(args, index1)
            push()