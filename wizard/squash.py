#!usr/bin/env python3
import subprocess


def add_file_and_commit(args, index):
    if any(arg == '-f' for arg in args):
        if index + 2 < len(args):
            file_to_add = args[index+1]
            commit_message = args[index+2]
            command = ['git', 'add', file_to_add]
            commit = ['git', 'commit', '-m', commit_message] # Try to commit just a file later
            try:
                subprocess.run(command, check=True)
                subprocess.run(commit, check=True)
                print(f"Successfully Committed {file_to_add}")

            except subprocess.CalledProcessError:
                pass
            except IndexError:
                print(f"List index is out of range,")
                print("Could be because arguments are not placed well") # Suggest to check documentation over here

    elif any(arg == '-fp' for arg in args) or any(arg == '-pf' for arg in args):
        if index + 2 < len(args):
            file_to_add = args[index+1]
            commit_message = args[index+2]
            command = ['git', 'add', file_to_add]
            commit = ['git', 'commit', '-m', commit_message] # try to commit one file
            try:
                subprocess.run(command, check=True)
                subprocess.run(commit, check=True)
                print(f"Successfully Committed {file_to_add}")

            except subprocess.CalledProcessError:
                pass
            except IndexError:
                print(f"List index is out of range,")
                print("Could be because arguments are not placed well")  # Suggest to check documentation over here
        
    else:
        print("No argument found")


# def add_file(args):
#     if any(arg == '-f' for arg in args):
#         index = args.index('-f')
#         file_to_add = args[index + 1]
#         command = ['git', 'add', file_to_add]
#         try:
#             subprocess.run(command, check=True)
#             print(f"""
#                   Successfully added {file_to_add}!
#                   Use squash -cp <commit-message> to commit and push all files
#                   """)
#         except subprocess.CalledProcessError as error:
#             print(f"{error}")
#     else:
#         print("No argument found")


def add_all_and_commit(args, index):
    if any(arg == '-a' for arg in args):
        commit_message = args[index + 1]
        command1 = ['git', 'add', '.']
        command2 = ['git', 'commit',  '-m', f'{commit_message}']
        try:
            subprocess.run(command1, check=True)
            subprocess.run(command2, check=True)
            print(f"Successfully committed all files")
        except subprocess.CalledProcessError:
            pass
        except IndexError:
            print(f"List index is out of range,")
            print("Could be because arguments are not placed well")  # Suggest to check documentation over here
            
    elif any(arg == '-ap' for arg in args) or any(arg == '-pa' for arg in args):
        if index:
            commit_message = args[index+1]
            command = ['git', 'add', '.']
            commit = ['git', 'commit', '-m', commit_message]  # try to commit one file
            try:
                subprocess.run(command, check=True)
                subprocess.run(commit, check=True)
                print(f"Successfully Committed files")
            except subprocess.CalledProcessError:
                pass
            except IndexError:
                print(f"List index is out of range,")
                print("Could be because arguments are not placed well")  # Suggest to check documentation over here
        

def push():
    command = ['git', 'push']
    try:
        subprocess.run(command, check=True)
        print(f"Commits have been pushed!")
    except subprocess.CalledProcessError as error:
        pass
    except IndexError:
        print(f"List index is out of range,")
        print("Could be because arguments are not placed well")  # Suggest to check documentation over here


# def timeTravel(commit_id):
#     commit_id = str(commit_id)
#     print(commit_id)


if __name__:
    print('gitWiz🪄')

