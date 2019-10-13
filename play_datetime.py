from datetime import date, timedelta

today = date.today()
print(today)
print(type(today))

birthday = date(year=1986, month=11, day=25)
print(birthday.strftime('%d, %B %Y'))
print(type(birthday))


print(today.year)
print(today.month)
print(today.day)

future_birthday = birthday.replace(year=today.year)
print(future_birthday)


print(today > birthday)
print(today > future_birthday)

# date object which is 2 week hence from today
one_week_hence = timedelta(weeks=2)
one_week_hence_date = today + one_week_hence

print(one_week_hence_date)

# date object which is 20 days back in the past from today
twenty_days_inpast = timedelta(days=-20)
twenty_days_inpast_date = today + twenty_days_inpast

print(twenty_days_inpast_date)