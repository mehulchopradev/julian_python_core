from com.abc.lib.banking.account import Account
from traceback import print_exc
from com.abc.lib.banking.exceptions.over_draft_error import OverdraftError

a1 = Account(acc_no='34567', acc_type='Savings', acc_balance=2000)

try:
  ub = a1.withdraw(1000)
except OverdraftError as e:
  print_exc()
  print(e.faulty_obj)
except ValueError:
  print_exc()
else:
  print(ub)