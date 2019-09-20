from .shape import Shape

class Rectangle(Shape):
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  # not followed the protocol
  # not overriden the method
  def area(self):
    return self.length * self.breadth

  def perimeter(self):
    return 2 * (self.length + self.breadth)