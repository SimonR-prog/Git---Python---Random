import datetime


from datetime import date
date = date.today()
print(date.weekday())


week = date.today().isocalendar()[1]

print(week)