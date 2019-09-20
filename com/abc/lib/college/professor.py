from .college_user import CollegeUser # . current directory
from ..email_sender.daily_email import DailyEmail # .. outside the current directory

# sub class/ child class
# Professor -> CollegeUser (single inheritance)
# Professor -> CollegeUser -> object (multilevel inheritance)
# Professor -> CollegeUser, DailyEmail -> (multiple inheritance)
class Professor(CollegeUser, DailyEmail):
  def __init__(self, name=None, gender=None, subjects=None, email=None, contact_nos=[]):
    super().__init__(name, gender, contact_nos)
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.subjects = subjects
    self.email = email

  def get_subjects(self):
    if self.subjects:
      return '|'.join(self.subjects)
    return 'NA'