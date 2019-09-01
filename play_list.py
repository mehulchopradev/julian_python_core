nos = [5, 6, 2, 3, 5, 10, 1]
# You
def for_each(elements, code):
  for element in elements:
    code(element)




# rest of the world
# prints all the elements in a list
print('All elements')

# Functions in python are treated as regular objects
def print_element(ele):
  print(ele)
for_each(nos, print_element) # Functional programming
# callback functions

'''for n in nos:
  print(n)'''


# print all the even elements from the list
print('Even elements')
def print_even(ele):
  if not ele % 2:
    print(ele)
for_each(nos, print_even)
'''for n in nos:
  if not n % 2:
    print(n)
'''

# callback function must have only one statement
print('All elements')
# lambda functions
# annonymous functions
# single statement functions
for_each(nos, lambda ele : print(ele))

print('Even  elements')
for_each(nos, lambda ele : print(ele) if not ele % 2 else print('', end=''))