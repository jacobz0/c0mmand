import os
import sys
import time


def slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()


def shut_down_cmd():
    shut_down = input("This will turn off the program. Enter 'y' or 'n': ")
    if shut_down == 'y':
        slow('>.')
        sys.exit()
    if shut_down == 'n':
        pass


def restart():
    print("Restarting..")
    time.sleep(3)
    os.system('python "C:/Users/Jacob Zhang/PycharmProjects/sys_c/System/command/startup.py')
