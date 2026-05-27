# "Duck Typing" = Another way to achieve polymorhpism besides inheritance
#                 Object must have the minimum necessaru attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must
#                 be a duck"


class Animal:
  alive = True

class Dog(Animal):
  def speak(self):
    print("WOOF")

class Cat(Animal):
  def speak(self):
    print('MEOW')

# does not inherit Animal class in argument list but has the basic attributes
class Car:
  alive = False
  def speak(self):
    print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
  animal.speak()
  print(f'{animal.alive}')
