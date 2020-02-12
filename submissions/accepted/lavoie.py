
months = {
    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11
}

doomsdays = [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

days = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

is_leap_year = lambda y: (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))
anchor_day = lambda y: (y / 100 % 4 * 5 % 7 + 2) % 7
doomsday = lambda y, a: (y + y / 4 + a) % 7

def get_week_day(day, month, year):
    a = anchor_day(year)
    d = doomsday(year % 100, a)
    doomsday_of_the_month = doomsdays[month]

    if month == 0 or month == 1:
        doomsday_of_the_month += 1 if is_leap_year(year) else 0
    
    if day >= doomsday_of_the_month:
        return (abs(day - doomsday_of_the_month) + d) % 7
    else:
        return (d - abs(day - doomsday_of_the_month)) % 7

n = int(raw_input())

days_of_week = [get_week_day(int(day), months[month], int(year)) for (day, month, year) in [raw_input().split() for i in xrange(n)]]

print("\n".join([days[day] for day in days_of_week]))

