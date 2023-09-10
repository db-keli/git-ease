#!/usr/bin/env python3

from Squasher.squash import *
import re
import sys
import subprocess


args = sys.argv

#Add a file and commit
for arg in args:
    match_AddAndCommit1 = re.findall('-', arg)
    match_AddAndCommit2 = re.findall('', arg)
    print(match_AddAndCommit1)

# if match_AddAndCommit1 != None:
#     print('This is when I do this shit')
#     print(args[1])

# #When arg is 
# if match_AddAndCommit2 !=None:
#     print 

if '-f' in args and '-p' in args:
    print('W')

elif '-fp' in args or '-pf' in args:
    print('L')