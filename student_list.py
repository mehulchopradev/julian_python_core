from com.abc.lib.college.student import Student


slist = [
  Student(name='mehul', roll=10, gender='m', marks=90),
  Student(name='jane', roll=2, gender='f', marks=80),
  Student(name='jill', roll=45, gender='f', marks=70)
]

# search by roll
roll = int(input('Enter roll to search : '))

for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  print('Student not found')