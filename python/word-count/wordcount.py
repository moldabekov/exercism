#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def word_count(s):
    counts = dict()
    words = re.findall('[a-z0-9а-я]+', s.lower())
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#print(word_count("до🖖свидания!"))
