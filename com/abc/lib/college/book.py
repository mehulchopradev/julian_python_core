class Book:
  def __init__(self, title, pages, price):
    self.title = title
    self.pages = pages  # @pages.setter
    # if pages object attribute needs to be given an encapsulated access; then 
    # make pages as private attribute but expose pages as a object property for the outside world
    # __pages - Object attribute
    # pages - Object property
    # Object property will proxxy all calls to object attribute
    # obj.pages = 900 -> do the checking -> obj.__pages = 900

    # self.__price = price # private attribute
    self.set_price(price)

  def __str__(self):
    return 'Title: {0}\nPages: {1}\nPrice: {2}'.format(self.title, self.pages, self.__price) # @property

  # encapsulation
  def set_price(self, price):
    if price < 0:
      raise ValueError('Price can be >= 0')
    self.__price = price

  def get_price(self):
    return self.__price

  @property
  def pages(self): # getter function
    # print(obj.pages)
    return self.__pages

  @pages.setter
  def pages(self, pages): # setter function
    # obj.pages = 900
    if pages <= 0:
      raise ValueError('Pages cannot be 0 or less than it')
    self.__pages = pages