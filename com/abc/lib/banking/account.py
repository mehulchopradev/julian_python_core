from .exceptions.over_draft_error import OverdraftError

class Account:
  def __init__(self, acc_no, acc_type, acc_balance):
    self.acc_no = acc_no
    self.acc_type = acc_type
    self.acc_balance = acc_balance

  def deposit(self, amt):
    self.acc_balance += amt
    return self.acc_balance

  def withdraw(self, amt):
    print('Transaction starts...')

    try:
      if amt <= 0:
        raise ValueError('Amt to withdraw should be greater than 0')
      if self.acc_balance - amt < 1000:
        # exceptional condition has occurred in the software
        # we look at returning from the function from this point itself
        # not by means of returning a value that the function promised with its normal return
        # raise ValueError('Balance of acc {0}, going below {1}'.format(self.acc_no, 1000))
        raise OverdraftError(msg='Balance of acc {0}, going below {1}'.format(self.acc_no, 1000), faulty_obj=self)
      self.acc_balance -= amt
      return self.acc_balance
    finally:
      # will execute irrespective of whether an error is thrown in the corresponding try block or not thrown (normal return)
      # finally has to be with a try block, try-except, try-except-else
      # most of resource closing code (server, file,) will be written here
      print('Transaction ends!')
  
  def __str__(self):
    return 'Acc No : {0}\nAcc bal : {1}'.format(self.acc_no, self.acc_balance)