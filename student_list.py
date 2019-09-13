from com.abc.lib.college.student import Student

sdict = {}

n = int(input('No of students : '))

for ii in range(1, n + 1):
  name = input('Enter name of student ' + str(ii))
  roll = int(input('Enter roll of student ' + str(ii)))
  gender = input('Enter gender of student ' + str(ii))
  marks = float(input('Enter marks of student ' + str(ii)))

  s = Student(name=name, roll=roll, gender=gender, marks=marks)

  sdict[roll] = s


'''slist = [
  Student(name='mehul', roll=10, gender='m', marks=90),
  Student(name='jane', roll=2, gender='f', marks=80),
  Student(name='jill', roll=45, gender='f', marks=70)
]'''

'''sdict = {
  10: Student(name='mehul', roll=10, gender='m', marks=90),
  2: Student(name='jane', roll=2, gender='f', marks=80),
  45: Student(name='jill', roll=45, gender='f', marks=70),
  20: Student(name='julian', roll=20, gender='m', marks=90)
}'''

# search by roll
roll = int(input('Enter roll to search : '))

if roll in sdict:
  student = sdict[roll]
  print(student.get_details())
else:
  print('Student not found')


'''for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  print('Student not found')'''
