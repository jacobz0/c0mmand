import os
import os.path
import requests
import subprocess
import time


def slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()


def directory_cmd():
    print(os.system('dir'))


def make_directory_cmd():
    try:
        new_file_location = input("""Entering no file directory but a name will place it in the current directory. 
Type directory to see the current directory. The name will be the input
(ENTERING NOTHING WILL NOT CREATE A NEW FILE)
Enter file directory: """)
        os.mkdir(new_file_location)
        print("File has been successfully created")
    except FileExistsError:
        print(f"The directory of {new_file_location} already exists.")
        pass
    except OSError:
        print(f"The syntax for {new_file_location} is incorrect.")
        pass


def downloader():
    try:
        input("Enter a download link: ")
    except requests.exceptions.MissingSchema:
        time.sleep(0.5)
        slow("A error occurred: Make sure you type in a valid link")
        pass


def launcher():
    try:
        application_opener_directory = input("Enter the directory for the app you want to launch: ")
        subprocess.Popen(application_opener_directory)
    except OSError:
        print("This application or directory does not exist or you do not permission to access this program/file.")
