#!/usr/bin/env python3

import random
import math

random.seed(1311)

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

def generate_case(filename, n):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        for i in range(n):
            day = 0
            year = random.randint(0,3000)
            month = MONTHS[random.randint(0,11)]

            if month == 'February':
               day = random.randint(1,28)
               if is_leap(year):
                   day += 1
            elif month in THIRTY_DAY:
               day = random.randint(1,30)
            else:
               day = random.randint(1,31)
            f.write(str(day) + " " + month + " " + str(year) + "\n")
        f.close()

generate_case("1-max.in", 10000)
