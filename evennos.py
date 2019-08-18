# Module name -> evennos

n = int(input('Enter n : '))

'''i = 0

while i <= n:
  if not i % 2:
    print(i)
  i = i + 1'''

# for loop
# for v in sequence of elements:
#    Inst1
#    Inst2
# Sequence of 10 elements - for loop move 10 times
# Sequence of 20 elements - for loop move 20 times
# 0-
# range(0, 5) -> [0, 1, 2, 3, 4]
# range(5) -> [0, 1, 2, 3, 4]

for v in range(0, n + 1):
  if not v % 2:
    print(v)