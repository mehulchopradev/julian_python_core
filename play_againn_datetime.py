from datetime import datetime

dt = datetime.now()

print(dt)
print(type(dt))

t = dt.time()
print(t)
print(type(t))

d = dt.date()
print(d)
print(type(d))

print(dt.year)
print(dt.month)
print(dt.hour)
print(dt.minute)