"""
Name: text_file_viewer.py
Author: Ezekiel Nieves 
Description:    This program views text files withinh a folder and the subdirectories.
                This program also reads  out text files within the directories but only if
                they possess a .txt extension.
                Other files are listed but they will be skipped.

"""

import os
def displayFiles(path_name):
    """
    Recursive fucntion that goes through a folder and lists the content within it. If it finds a .txt file it prints its contents
    """
    pass
    if not os.path.isdir(path_name):
        # Base case
        # This process makes a tuple out of the path and gets the final element of 
        # an Rsplit which would be the name of the file
        path_name = str(path_name)
        path_tuple = path_name.rsplit(os.sep)
        file_name = path_tuple[len(path_tuple) - 1]
        print(file_name)
        extension = file_name.rsplit('.')
        if extension[len(extension) - 1] == "txt":
            f = open(path_name, 'r')
            print(f.read())
            f.close()
            return
    else: 
        # recursive case
        dir_list = os.listdir(path_name)
        print(dir_list)
        for file in dir_list:
            file_path = path_name + os.sep + file
            displayFiles(file_path)


def main():
    pass
    path_name = str(input("Enter a path name: "))
    displayFiles(path_name)

if __name__ == "__main__":
    main()