from com.abc.lib.college.book import Book

b1 = Book(title='Book 1', pages=190, price=1000)
# print(b1.__price) # cannot access private attribute from outside
# b1.__price = -900 # cannot access private attribute from outside

# 1.price = 600 # will not work
b1.set_price(600)

# b1.set_price(-900)

print(b1)
print(b1.get_price())
# print(b1.price)

print(b1.pages)
b1.pages = 800
print(b1)

b1.pages = -450
print(b1)