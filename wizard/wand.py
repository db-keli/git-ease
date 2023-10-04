#!/usr/bin/env python3

from squash import add_all_and_commit, add_file_and_commit, push
import re
import sys


def main():
    args = sys.argv

    # Add one file and commit/commit and push 

    # When there's only -f argument(add and commit only)

    match1 = None
    match2 = None

    if args[1] == '-f' and args[2] != '-p':
        index = args.index('-f')
        add_file_and_commit(args, index)

    # When arguments begin with -f -p
    elif args[1] == '-f' and args[2] == '-p':
        index = args.index('-p')
        add_file_and_commit(args, index)
        push()

    # When arguments begin with -fp or -pf(add, commit and push)   
    elif (re.search('-fp', arg) for arg in args) or (re.search('pf', arg) for arg in args):
        for arg in args:
            match1 = re.findall('-fp', arg)
            match2 = re.findall('-pf', arg)
        
        if match1:
            index1 = args.index('-pf')
            add_file_and_commit(args, index1)
            push()
        elif match2:
            index2 = args.index('-fp')
            add_file_and_commit(args, index2)
            push()

    # Add all files and commit/commit and push

    # When arguments begin with -a only(add and commit only)
    if args[1] == '-a':
        index = args.index('-a')
        add_all_and_commit(args, index)

    # When arguments begin with -a -p(add, commit and push them)
    elif args[1] == '-a' and args[2] == '-p':
        index = args.index('-p')
        add_all_and_commit(args, index)
        push()

    # When arguments begin with -ap or -pa(add, commit and push files)
    elif (re.search('-ap', arg) for arg in args) or (re.search('-pa', arg) for arg in args):
        for arg in args:
            match1 = re.findall('-ap', arg)
            match2 = re.findall('-pa', arg)

        if match1 is not None:
            try:
                index1 = args.index('-ap')
                add_all_and_commit(args, index1)
                push()
                print("shit worked")
            except ValueError:
                pass

        if match2 is not None:
            try:
                index2 = args.index('-pa')
                add_all_and_commit(args, index2)
                push()
            except ValueError:
                pass


if __name__ == '__main__':
    main()
