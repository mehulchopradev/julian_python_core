from traceback import print_exc

print('Program starts')

n = input('enter n : ')

# exception handling
try:
  ni = int(n)
except ValueError:
  # print('Hey enter only integers')
  print_exc()
else:
  # when there is no exception thrown in the corresponding try block
  print('odd') if ni % 2 else print('Even')

print('Program ends')