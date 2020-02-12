#!/usr/bin/python2
from sys import stdin
import sys
import re

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

THIRTY_DAY = [
    'September',
    'April',
    'June',
    'November'
]

is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

integer = "[1-9][0-9]*"
date = "^[1-3]?[0-9] (January|February|March|April|May|June|July|August|September|October|November|December) [1-3]?[0-9]?[0-9]?[0-9]\n$"

lines = stdin.readlines()

assert re.match(integer + "\n", lines[0])
n = int(lines[0][:-1])
assert 1 <= n <= 10000
assert len(lines) == n + 1
i = 0

for i in range(1, n + 1):
    try:
        assert re.match(date, lines[i])
        (day, month, year) = lines[i][:-1].split()
        (day, year) = map(int, [day, year])

        assert month in MONTHS
        
        if month == 'February' and not is_leap(year):
            assert day in range(1,29)
        elif month == 'February':
            assert day in range(1,30)
        elif month in THIRTY_DAY:
            assert day in range(1,31)
        else:
            assert day in range(1,32)

        assert 0 <= year <= 3000
    except AssertionError:
        print lines[i]

# All good
sys.exit(42)
