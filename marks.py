'''
 >= 70 - A
 >= 60 - B
 >= 40 - C
 < 40 - F
 < 0 or > 100 - I
'''
marks = float(input('Enter marks : '))

if marks < 0 or marks > 100:
  print('I')
elif marks >= 70:
  print('A')
elif marks >= 60:
  print('B')
elif marks >= 40:
  print('C')
else:
  print('F')