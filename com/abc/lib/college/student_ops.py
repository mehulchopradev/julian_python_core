def get_details(name, gender, roll, marks):
  return 'Name : ' + str(name) + '\nGender : ' + str(gender) + '\nRoll : ' + str(roll)\
    + '\nMarks : ' + str(marks)

def get_grade(marks):
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