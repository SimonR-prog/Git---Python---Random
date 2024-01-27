def current_week():
    from datetime import date
    week = date.today().isocalendar()[1]
    return week




print(current_week())




def current_day():
    from datetime import date
    date = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = weekdays[(date.weekday())]
    return day


print(current_day())