a = 11 # entire module
count = 0 # entire module

def abc():
  i = 5 # local variable to the abc()
  j = 10 # local variable to the abc()
  
  global count
  count = count + 1 # modify the module level variable count

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
abc()

print(count)
# print(i) # i scope is only abc()

# variable scope in python is
# 1. function scope
# 2. module scope


def mno():
  i = 9 # mno

  def pqr(): # mno
    print(i) # 9
    return 10

  return pqr # a function can return another function from itself


p = mno()
# p is a callable variable
# bcoz stores the address of a function object
r = p() # pqr()
print(r)



def fun(f):
  # f to be a callable variable
  # f to store the address of a function object
  r = f() # rrr()
  return r + 10

def rrr():
  return 20

result = fun(rrr) # passing a function as an argument to another function
print(result)

result = fun(lambda : 40)
print(result)










