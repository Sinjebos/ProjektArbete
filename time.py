import datetime
import time


def isMidnight():
    last_day = datetime.datetime.now().day
    day = datetime.datetime.now().day
    if day != last_day:
        last_day = day
        
