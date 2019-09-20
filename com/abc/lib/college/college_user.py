# super class
# parent class
class CollegeUser: # class CollegeUser(object)
  def __init__(self, name, gender, contact_nos):
    # self - Student object
    # self - Professor object
    # self - Can be any subclass/child class object of CollegeUser
    self.name = name
    self.gender = gender
    self.contact_nos = contact_nos

  def get_details(self):
    # self - Can be any subclas/child class object of CollegerUser
    part1 = 'Name : {0}\nGender : {1}\n'.format(self.name, self.gender)

    part2 = 'Contact Nos -> \n'
    if self.contact_nos:
      '''for contact_no in self.contact_nos:
        str2 += str(contact_no) + '\n'
      '''
      part2 += '\n'.join(self.contact_nos)
    else:
      part2 += 'NA'
    
    return part1 + part2

  # overriden
  def __str__(self):
    return 'Name : {0}\nGender : {1}\n'.format(self.name, self.gender)