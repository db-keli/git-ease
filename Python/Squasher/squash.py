#!usr/bin/env python3
import subprocess
import sys


def add_file_commit(args):
    if any(arg == '-f' for arg in args):
        index = args.index('-f')
        if index + 2 < len(args):
            file_to_add = args[index+1]
            commit_message = args[index+2]
            command = ['git', 'add', file_to_add]
            commit = ['git', 'commit', '-m', commit_message]
            try:
                subprocess.run(command, check=True)
                print(f"""
                      Successfully added {file_to_add}! 
                      Simply use git push to push all files!
                      """)
                subprocess.run(commit, check=True)
                print(f"Committed {file_to_add}")

            except subprocess.CalledProcessError as error:
                print(f"{error}")
    else:
        print("No argument found")


def add_file(args):
    if any(arg == '-f' for arg in args):
        index = args.index('-f')
        file_to_add = args[index + 1]
        command = ['git', 'add', file_to_add]
        try:
            subprocess.run(command, check=True)
            print(f"""
                  Successfully added {file_to_add}!
                  Use squash -cp <commit-message> to commit and push all files
                  """)
        except subprocess.CalledProcessError as error:
            print(f"{error}")
    else:
        print("No argument found")


def add_all(args):
    if any(arg == '-a' for arg in args):
        command = ['git', 'add', '.']
        try:
            subprocess.run(command, check=True)
            print(f"Successfully added all files!")
        except subprocess.CalledProcessError as error:
            print(f"{error}")

if __name__ == "__main__":
    add_file(sys.argv)

