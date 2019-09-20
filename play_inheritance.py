# vendor 1
class Abc:

  def fun(self):
    return 'fun'

  def go(self):
    return 'totally different implementation'

# vendor 2
class Pqr:

  def go(self):
    return 'go'

# You
# child class -> more than 1 -> parent class (multiple inheritance)
class Mno(Pqr, Abc): # MRO (Method resolution order)
  pass



m = Mno()
print(m.fun())
print(m.go())