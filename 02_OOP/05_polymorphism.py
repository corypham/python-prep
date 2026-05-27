# Polymorphism = Greek word that means to have "many forms or faces"
#                Poly = many
#                Morphe = Form
#
# Two ways to achieve polymorphism:
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. Duck typing = Object must hace necessaru attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius) -> None:
    self.radius = radius

  def area(self):
    return 3.14 * self.radius

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

class Triange(Shape):
  def __init__(self, base, height) -> None:
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height * 0.5

# Pizza takes on three forms: pizza, circle, shape
class Pizza(Circle):
  def __init__(self, topping, radius) -> None:
    super().__init__(radius)
    self.topping = topping


shapes = [Circle(4), Square(5), Triange(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
  print(f'{shape.area()}')