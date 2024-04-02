"""   
7. Write a function findfiles that recursively descends the directory tree for the specified
directory and generates paths of all the files in the tree.

"""
import os

def find_files(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

directory = input("Enter the directory path: ")

if os.path.isdir(directory):
    
    file_paths = find_files(directory)
    print("Files in directory tree:")
    for file_path in file_paths:
        print(file_path)
else:
    print("Invalid directory path.")
