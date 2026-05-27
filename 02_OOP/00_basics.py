# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# dunder method = double underscore

# self = this object were creating right now

class Car:
  # constructor method in order to create objects
  def __init__(self, model, year, color, for_sale = True):
    self.model = model
    self.year = year
    self.color = color            
    self.for_sale = for_sale

  def drive(self):
    print(f'You are driving the {self.color} {self.model}')
  
  def stop(self):
    print(f'You are stopping the {self.color} {self.model}')

  def describe(self):
    print(f'Model: {self.model}')
    print(f'Year: {self.year}')
    print(f'Color: {self.color}')
    print(f'For Sale: {self.for_sale}')

if __name__ == "__main__":
  car1 = Car("Tesla", 2024, "red", False)
  car2 = Car("corvette", 2022, "blue", True)
  car3 = Car("Charger", 2026, "black")
  print(car1)
  print(car1.model)

  car1.drive()

  car1.stop()

  car1.describe()