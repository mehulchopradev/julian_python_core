from pathlib import Path
from shutil import copy
from com.abc.lib.series import get_fibo_series

input_path = input('Enter the full file path from where u want to copy : ')
output_dir = input('Enter the full dir path to which you want to copy : ')


p1 = Path(input_path)
p2 = Path(output_dir)

if not p1.exists():
  print('Please enter the right input path')
else:
  input_name = p1.name
  if p2.exists() and p2.is_dir():
    output_file_path = '{0}/{1}'.format(output_dir, input_name)

    # single threaded fashion
    # sequential execution
    copy(input_path, output_file_path) # IO operation
    # 10 MB file or more
    # CPU is free (idle)
    print('Copying done!')

    n = 30
    print(get_fibo_series(n)) # CPU operation
  else:
    print('Please enter right output dir path')