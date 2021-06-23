#!/usr/bin/python3

import os
import random
import string

script_path = os.getcwd() # Curent script path
files_path = os.path.join(script_path, "items\\") # There indicate a path to folder where is files ready to randomize names
print(files_path)


def create_rand_name(path, ext):
    rand_file_name = ""
    check = False
    while not check:
        rand_file_name = "".join(random.sample(string.ascii_lowercase + string.digits, 20)) + ext
        check = True if not os.path.exists(path + rand_file_name) else False
    return rand_file_name


def do_rename(path):
    print("Begin renaming...")
    # Rename everything in target folder
    for item in os.listdir(path):
        if os.path.isfile(path + item):
            # Get a random name including the previous file extension
            rand = create_rand_name(path, os.path.splitext(item)[1])
            # Do the rename
            os.rename(path + item, path + rand)
            print("Renaming:", item, "to ", rand, " - Done.")
        else:
            # Not a file
            print("\tSkipped:", "'" + item + "'", "Target is not a file")


def main():
    do_rename(files_path)


main()
