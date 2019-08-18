n = int(input('Enter n : '))

'''if n % 2:
  print('It is odd')
else:
  print('It is even')'''

# if comprehensions
# Both the branches must have only one executable statement
print('It is odd') if n % 2 else print('It is even')