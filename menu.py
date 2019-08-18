# Module name -> menu

'''
1. Fibo Series
2. Even Series
3. Even or odd
4. Factorial
5. Exit
Please enter ur choice : 1
Enter n : 8
0 1 1 2 3 5 8 13
1. Fibo Series
2. Even Series
3. Even or odd
4. Factorial
5. Exit
Please enter ur choice : 2
Enter n : 10
0 2 4 6 8 10
1. Fibo Series
2. Even Series
3. Even or odd
4. Factorial
5. Exit
Please enter ur choice : 3
Enter n : 11
Its odd
1. Fibo Series
2. Even Series
3. Even or odd
4. Factorial
5. Exit
Please enter ur choice : 4
Enter n : 6
720
'''

# import the module
# import series
import math # built in module
import com.abc.lib.math # user defined module

# directly import the functions from the module
from com.abc.lib.series import get_fibo_series as get_fibo, get_even_series

while True:
  print('1. Fibo Series\n2. Even Series\n3. Even or odd\n4. Factorial\n5. Exit')
  choice = int(input('Please enter ur choice : '))
  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    n = int(input('Enter n : '))

  if choice == 1:
    print(get_fibo(n))
    # pass # allows empty blocks
  elif choice == 2:
    print(get_even_series(n))
  elif choice == 3:
    print(com.abc.lib.math.is_even_odd(n))
  elif choice == 4:
    print(math.factorial(n))
  else:
    # something ?
    break