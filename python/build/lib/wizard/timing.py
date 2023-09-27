import datetime

def date_commited():
    whole_date = datetime.datetime.now()
    actual_date = whole_date.strftime('%Y-%m-%d')
    return actual_date

def time_commited():
    actual_time = datetime.datetime.now().strftime('%I:%M %p')
    return actual_time

def day_commited():
    day = datetime.datetime.now().strftime('%A')
    return day

print(f"Commited this on {date_commited()} {day_commited()}, at {time_commited()} ")

