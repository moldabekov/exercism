#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


def add_gigasecond(x):
    return x + timedelta(seconds=10**9)
