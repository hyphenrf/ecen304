"""
Utility functions for the backend. 
"""

import datetime
from time import time

def _serialize(obj):
    return obj.__dict__

def _salt(name: str) -> str:
    return "".join(map(lambda x: str(ord(x)), name))

def _verify_date(date):
    #TODO: refactor this out -- use EPOCH ints.
    day, month, year = date.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate == False):
        raise Exception("Input date is not valid..")
    else:
        return date

def _time() -> int:
    return int(time())

def _seconds_of_days(days: int) -> int:
    return days * 24 * 60 * 60
