from com.abc.lib.geometry.square import Square
from com.abc.lib.geometry.rectangle import Rectangle
from com.abc.lib.geom_stats.print_stats import PrintStats

s = Square(side=5)
# print(s.area())
# print(s.perimeter())

PrintStats.print(s)


r = Rectangle(length=8, breadth=2)

PrintStats.print(r)