#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Skeleton file for the Python "Bob" exercise.
#

import re


def hey(what):

    what = what.lstrip().rstrip()
    capital = re.findall(ur'[A-ZА-Я]+', what)
    lower = re.findall(ur'[a-zа-я]+', what)

    if len(what) == 0:
        return 'Fine. Be that way!'

    if (len(lower) == 0) and (len(capital) > 0):
        return 'Whoa, chill out!'

    if (len(what) != 0) and (what[len(what) - 1] == '?'):
        return 'Sure.'

    return 'Whatever.'

# print (hey('ÜMLäÜTS'))
