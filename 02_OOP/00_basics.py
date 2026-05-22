# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# dunder method = double underscore

# self = this object were creating right now
class Car:
  # constructor method in order to create objects
  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

if __name__ == "__main__":
  car1 = Car("Tesla", 2024, "red", False)
  print(car1)
  print(car1.model)