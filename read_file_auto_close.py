path = '/Users/mehul.chopra/Documents/professor.py'

with open(path) as fp:
  # with occupying resource
  # coming out of with, the resource occupied will be auto closed
  for line in fp:
    print(line)