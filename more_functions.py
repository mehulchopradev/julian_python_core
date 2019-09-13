# variable numbers of arguments (0 to n)
def myadd(*args):
  # all the arguments passed, get packed into the args tuple object
  # print(args) # tuple
  sum = 0
  for item in args:
    sum += item
  return sum

# positional arguments packing
print(myadd())
print(myadd(4, 5))
print(myadd(5, 6, 3, 4, 10))

def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = [9, 4] # can even be a tuple
print(perimeter(stats[0], stats[-1]))
print(perimeter(*stats)) # positional argument unpacking

def area(**rect_stats):
  # print(rect_stats) # dict
  return rect_stats['length'] * rect_stats['breadth']

# print(area(5.1, 4.9))
print(area(length=5.1, breadth=4.9)) # keyword arguments packing
# print(area(len=5.1, bre=4.9)) # this will not work


smap = {'breadth': 5, 'length': 6}

print(perimeter(smap['length'], smap['breadth']))
print(perimeter(**smap)) # keyword arguments getting unpacked