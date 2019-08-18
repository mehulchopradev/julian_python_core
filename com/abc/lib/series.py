# Module name -> series

def get_fibo_series(n):
  result = ''
  a, b = 0, 1
  result += str(a) + '\t' + str(b) + '\t'

  for v in range(3, n + 1):
    c = a + b
    result += str(c) + '\t'
    a, b = b, c
  return result

def get_even_series(n):
  result = ''
  for i in range(0, n + 1, 2):
    result += str(i) + '\t'

  return result