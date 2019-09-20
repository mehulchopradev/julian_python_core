from com.abc.lib.college.professor import Professor
from com.abc.lib.college.student import Student

p1 = Professor('mehul', 'm', ['Physics', 'Maths'], 'mehul.chopra.dev@gmail.com')
p1.send_daily_email('Hi. This is ur daily news letter')
# Professor.send_daily_email(p1, 'Hi. This is ur daily news letter')
# DailyEmail.send_daily_email(p1, 'Hi. This is ur daily news letter')

# 1. Reserve an area in the memory for Professor - 2345
# 2. Professor.__init__(2345, 'mehul', 'm', ['Physics'])
# print(p1.name)
# print(p1.gender)

# print(p1.get_details())
# print(p1.get_subjects())
# Professor.get_details(p1)
# CollegerUser.get_details(p1)

s1 = Student('julian', 'm', 10, 93, ['98789789', '986868898'])

# print(s1.get_details())
# Student.get_details(s1)

i = 10

print(i)
# int.__str__(i)

print(p1) # name, gender
# Professor.__str__(p1)

print(s1) # name, gender, roll
# Student.__str__(s1)