#!/usr/bin/env python


def is_pangram(s):
    return not set(list(map(chr, range(97, 123)))) - set(s.lower())
