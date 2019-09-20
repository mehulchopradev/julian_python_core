from abc import ABC, abstractmethod # Abstract base class

# abstractmethod = decorator

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass