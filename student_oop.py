from com.abc.lib.college.student import Student

# print(Student.count) # accessing the class attribute
print(Student.get_count()) # accessing a class function
# Python internally
# Student.get_count()

s3 = Student()
print(s3.get_details())
print(s3.get_grade())
# Python do internally
# 1. Reserve some memory in the RAm - 6000
# 2. Student.__init__(6000)


s1 = Student('mehul', 10, 'm', 90)
# Python do internally
# 1. Reserve some memory in the RAM - 3000
# 2. Student.__init__(3000, 'mehul', 10, 'm', 90)
'''s1.name = 'mehul'
s1.roll = 10
s1.gender = 'm'
s1.marks = 90'''

print(Student.count)



s2 = Student('jane', 11, 'f', 60, ['93847395','54645646'])
'''s2.name = 'jane'
s2.r = 11
s2.gen = 'f'
s2.m = 60'''

#print(s1.name)
#print(s2.name)
#print(s2.roll)


print(s2.get_details())
# Python do internally
# Student.get_details(s2)

print(s1.get_details())
# Python do internally
# Student.get_details(s1)

print(s1.get_grade())
print(s2.get_grade())
# Python internally
# Student.get_grade(s1)

print(Student.count)

s4 = Student(name='julian', contact_nos=['8687868'], roll=34, gender='m')
print(s4.get_details())