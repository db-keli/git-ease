import datetime


def date_committed():
    whole_date = datetime.datetime.now()
    actual_date = whole_date.strftime('%Y-%m-%d')
    return actual_date


def time_committed():
    actual_time = datetime.datetime.now().strftime('%I:%M %p')
    return actual_time


def day_committed():
    day = datetime.datetime.now().strftime('%A')
    return day


print(f"Committed this on {date_committed()} {day_committed()}, at {time_committed()} ")

