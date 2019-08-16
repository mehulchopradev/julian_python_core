def perimeter_rectangle(length, breadth):
  p = 2 * (length + breadth)
  return p

def area_rectangle(length, breadth):
  a = length * breadth
  return a

l = float(input('Enter length : '))
b = float(input('Enter breadth : '))

p = perimeter_rectangle(l, b)
a = area_rectangle(l, b)

print(p)
print(a)