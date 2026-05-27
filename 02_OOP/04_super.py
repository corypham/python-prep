# super() = Function used in a child class to call methods from a parent class
#           (superclass). Allows you to extend the functionality of the
#           inherited methods


class Shape:
  def __init__(self, color, is_filled) -> None:
    self.color = color
    self.is_filled = is_filled

  def describe(self) -> None:
    print(f'It is {self.color} and {"filled" if self.is_filled else "not filled"}')

class Circle(Shape):
  def __init__(self, color, is_filled, radius) -> None:
    super().__init__(color, is_filled)
    self.radius = radius

  # method overriding 
  def describe(self) -> None:
    print(f'It is a circle with an area {3.14 * self.radius * self.radius}cm^2')

    # if you want to extend the functionality of the parent's attribute
    super().describe()

class Triangle(Shape):
  def __init__(self, color, is_filled, width, height) -> None:
    super().__init__(color, is_filled)
    self.width = width
    self.height = height

  def describe(self) -> None:
    print(f'It is a triangle with an area {0.5 * self.height * self.width}cm^2')
    super().describe()

circle = Circle("Red", True, 5)
triangle = Triangle(color="Blue", is_filled=False, width=5, height=7)

print(f'{circle.color}')
print(f'{circle.is_filled}')
print(f'{circle.radius}')

circle.describe()
triangle.describe()
# -------------------------------------------------------------------

class Rectangle:
  def __init__(self, width, length) -> None:
    self.width = width
    self.length = length

class Square(Rectangle):
  def __init__(self, width) -> None:
    super().__init__(width, width)

square = Square(5)

print(square.width * square.length)