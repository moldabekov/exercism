#!/usr/bin/env python


def distance(s, s2):
    if len(s) != len(s2):
        return 'Can`t calculate hamming distance'
    return sum(1 for i, j in zip(s, s2) if i != j)
