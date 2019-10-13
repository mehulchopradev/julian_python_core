from .college_user import CollegeUser

class Student(CollegeUser):
  def __init__(self, name=None, gender=None, roll=None, marks=None, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    self.roll = roll
    self.marks = marks

  # method overriding
  def get_details(self):
    #self - Will and awill always be a Student object
    part1 = super().get_details()
    # CollegerUser.get_details(self)

    # your own implementation
    part2 = '\nRoll : {0}'.format(self.roll)

    # inherited implementation + my own implementation
    return part1 + part2

  def __str__(self):
    return super().__str__() + 'Roll : {0}'.format(self.roll)

  def __gt__(self, other):
    return self.marks > other.marks

  def __lt__(self, other):
    return self.marks < other.marks

  def __lshift__(self, contact_no):
    self.contact_nos.append(contact_no)
    return self

  def __eq__(self, other):
    return self.roll == other.roll