#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import groupby


def encode(s):
    a = [(len(list(count)), char) for char, count in groupby(s)]
    # This one liner fails on one test with unicode input.
    # Windows is hell for UTF-8
    # return ''.join([str(i) for sub in a for i in sub if i != 1])
    res = ''
    for i, j in a:
        if i > 1:
            res += str(i)
        res += j
    return res


def decode(s):
    res = counter = ''
    for i in s:
        if i.isdigit():
            counter += i
        if i.isalpha() or i.isspace():
            if counter != '':
                res += int(counter) * i
                counter = ''
            else:
                res += i
    return res
