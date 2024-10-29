import time
from datetime import datetime
my_time = input("Enter (q to quit): ")

while not my_time =="q":

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time_frame = current_time.split(":")

    current_hour = int(current_time_frame[0])
    current_minutes = int(current_time_frame[1])
    current_seconds = int(current_time_frame[2])
    start_time = current_hour * 3600 + (current_minutes * 60) + current_seconds

    seconds = start_time % 60
    minutes = int (start_time / 60) % 60
    hours = int(start_time / 3600)
    if hours >= 24:
         hours = hours % 24
    time.sleep(1)
    start_time = +1
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
