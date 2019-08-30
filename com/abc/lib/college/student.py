class Student:
  count = 0 # class attribute

  def __init__(self, name=None, gender=None, roll=None, marks=None): # constructor overloading
    # None -> Variable is created but with no value (no address/no object)
    # None -> falsy in python

    # called during object creation
    # create attributes in an object

    # constructor

    # attributes of the object
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    Student.count += 1 # access class attriute using the class name

  def get_count():
    # class functions
    # does not have self
    return Student.count

  def get_details(self):
    return 'Name : ' + str(self.name) + '\nGender : ' + str(self.gender) + '\nRoll : ' + str(self.roll)\
    + '\nMarks : ' + str(self.marks)

  def get_grade(self):
    marks = self.marks
    if not marks: # None protection
      print('Cannot compute grade')
      return None

    if marks < 0 or marks > 100:
      return 'I'
    elif marks >= 70:
      return 'A'
    elif marks >= 60:
      return 'B'
    elif marks >= 40:
      return 'C'
    else:
      return 'F'