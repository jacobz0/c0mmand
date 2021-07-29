import time
import file_management
import help_command
import power
import system_information
import date_and_time
from colorama import Fore
import sys

print(sys.path)
print("Python 3.8.2 [2020]")


def slow(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)


def main_cmd():
    print("Welcome to Jacob's CMD. Enter help for help.")
    while True:
        prompt = input(Fore.RESET + "> ").upper().replace(" ", "")
        if prompt not in help_command.command_list:
            print(Fore.RED + "I don't know that word.")
        if prompt == 'TIME':
            date_and_time.time_cmd()
        if prompt == 'HELP':
            help_command.help_cmd()
        if prompt == 'DIRECTORY':
            file_management.directory_cmd()
        if prompt == 'SHUT DOWN':
            power.shut_down_cmd()
        if prompt == 'SET ALARM':
            date_and_time.alarm_cmd()
        if prompt == 'SYSTEM':
            system_information.basic_system_infor_cmd()
        if prompt == 'SYSTEM INFO':
            system_information.system_infor_cmd()
        if prompt == 'CALENDAR':
            date_and_time.calendar_cmd()
        if prompt == 'DATE':
            print(time.asctime())
        if prompt == 'MAKE DIRECTORY':
            file_management.make_directory_cmd()
        if prompt == 'ADVANCED SYSTEM INFO':
            system_information.advanced_system_infor_cmd()
        if prompt == 'DOWNLOAD':
            file_management.downloader()
        if prompt == 'RUN':
            file_management.launcher()
        if prompt == 'RESTART':
            power.restart()


main_cmd()
