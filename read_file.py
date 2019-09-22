path = '/Users/mehul.chopra/Documents/professor.py'

fp = open(path)
# print(type(fp))
# print(fp)

# soomething with fp
# read line by line
'''print('Read first time from the file')
for line in fp:
  print(line.rstrip()) # strips out the \n from the end of the line

print('Read second time from the file')
for line in fp:
  # wont go in the for loop
  # because of the previous loop which caused the internal file pointer to reach the end of file
  print(line.rstrip())

fp.seek(0) # take the file pointer to the start of the file
print('Read third time from the file')
for line in fp:
  # wont go in the for loop
  # because of the previous loop which caused the internal file pointer to reach the end of file
  print(line.rstrip())'''


'''lines = fp.readlines()
# takes the internal file pointer to the end of file
# be careful when using this method. You may hit OOM because of the list object being created in the ram

print(lines)'''

file_content = fp.read()
# takes the internal file pointer to the end of the file
# be careful when using this method. You may hit OOM because of the list object being created in the ram
# print(file_content)
# print(type(file_content))




# when done
fp.close()