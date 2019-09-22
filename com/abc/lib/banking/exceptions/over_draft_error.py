class OverdraftError(Exception):
  def __init__(self, msg, faulty_obj=None):
    super().__init__(msg)
    self.faulty_obj = faulty_obj