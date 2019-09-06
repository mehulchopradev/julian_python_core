# for comprehesions

nos = [4, 5, 2, 6, 10, 1, 3]

# a new list from the nos list consiting of only odd numbers (filtering)
'''odds = []
for n in nos:
  if n % 2:
    odds.append(n)

print(odds)'''

odds = [element for element in nos if element % 2]
print(odds)


# a new list from the nos list consisting of even numbers greater than 4 (filtering)
evens = [element for element in nos if not element % 2 and element > 4]
print(evens)

# a new list from the nos list consisting of squares of elements (mapping)
squares = [element ** 2 for element in nos]
print(squares)

# a new list from the nos list consisting of cubes of even numbers greater than 4 (filtering + mapping)
cubes = [element ** 3 for element in nos if not element % 2 and element > 4]
print(cubes)