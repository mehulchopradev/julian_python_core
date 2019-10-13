from com.abc.lib.college.student import Student

s1 = Student(name='mehul', gender='m', roll=10, marks=90, contact_nos=[])
s2 = Student(name='julian', gender='m', roll=11, marks=86, contact_nos=[])

# print(s1.marks > s2.marks)
print(s1 > s2) # operator overloading
# Internally
# print(s1.__gt__(s2))
# print(Student.__gt__(s1, s2))

print(s1 < s2)
# Internally
# print(s1.__lt__(s2))
# print(Student.__lt__(s1, s2))

# s1.contact_nos.append('8786876')
# s1.contact_nos.append('4456546')

# DSL (domain specific language)
s1 << '986786868'
# s1.__lshift__('986786868')
# Student.__lshift__(s1, '986786868')

s2 << '768768687' << '987867576576'

print(s1.get_details())
print(s2.get_details())

s3 = Student(name='Julian', gender='Male', roll=11, contact_nos=[])

print(s2 == s3)
# print(s2.__eq__(s3))
# print(Student.__eq__(s2, s3))

