#!/usr/bin/env python


def is_leap_year(date=0):
    if (date % 4 == 0) and (date % 100 == 0) and (date % 400 == 0):
        return True
    elif (date % 4 == 0) and (date % 100 != 0):
        return True
    else:
        return False
