from .shape import Shape

class Square(Shape):
  def __init__(self, side):
    self.side = side

  # followed the protocol laid by the super class
  # overriden those functions
  def area(self):
    return self.side * self.side

  def perimeter(self):
    return 4 * self.side