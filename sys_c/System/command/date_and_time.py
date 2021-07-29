from datetime import datetime, date

import calendar
import pyinputplus
import time
import winsound


def alarm_cmd():
    time_count = pyinputplus.inputInt("Enter a time in seconds\n")
    while time_count > 0:
        print(time_count)
        time.sleep(1)
        time_count = time_count - 1
    print('Alarm is off')
    loop = 0
    while loop < 10:
        frequency = 500  # 500 Hertz
        duration = 750  # 750 ms to seconds = 0.75 seconds
        winsound.Beep(frequency, duration)
        loop += 1


def time_cmd():
    clock = datetime.now()
    time_c = clock.strftime("%H:%M:%S")
    convert_time = datetime.strptime(time_c, "%H:%M:%S")
    print(convert_time.strftime("%r"))


def calendar_cmd():
    current_date = date.today()
    year = current_date.year
    month = current_date.month
    print(calendar.month(year, month))
