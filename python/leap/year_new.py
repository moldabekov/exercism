#!/usr/bin/env python


def is_leap_year(year):
    if (year % 100 == 0):
        return year % 400 == 0
    else:
        return year % 4 == 0
