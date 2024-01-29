

print(current_week())

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = weekdays[(date.weekday())]


def current_day():
    from datetime import date
    date = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = weekdays[(date.weekday())]
    return day


print(current_day())