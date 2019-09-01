a = 11 # entire module

def abc():
  i = 5 # local variable to the abc()
  j = 10 # local variable to the abc()

  def xyz():
    # print(i) # inner function can access the enclosing function variables
    i = 6 # local variable to the xyz()
    print('xyz')
    print(i) # 6
    print(j) # 10 inner function can access the enclosing function variables (closures)
  
  xyz()
  print(i) # 5
  print(a) # 11

abc()
# print(i) # i scope is only abc()

# variable scope in python is
# 1. function scope
# 2. module scope