import os
import re


def test():
    pass


def add_file_commit(*args):
    if re.search('^-f', args[1]):
        os.system(f'git add {args[2]}')


def add_all_commit(*args):
    return re.search('^-a', args[1])


add_file_commit('-f', '__init__.py', 'My name is mike')
