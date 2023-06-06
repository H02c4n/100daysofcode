import datetime as dt

now = dt.datetime.now()
year = now.year
mont = now.month
day_of_week = now.weekday()


print(now)
print(year)
print(day_of_week)


date_of_birth = dt.datetime(year=1987, month=12, day=12)

print(date_of_birth)