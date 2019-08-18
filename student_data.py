from com.abc.lib.college.student_ops import get_details, get_grade

name = input('Enter name : ')
roll = int(input('Enter roll : '))
marks = float(input('Enter marks : '))
gender = input('Enter gender : ')

print(get_details(name=name, roll=roll, marks=marks, gender=gender))
print(get_grade(marks=marks))