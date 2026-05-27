# Inheritance = Allows a class to inherit attrubutes and methods from
#               another class. Helps with code readabilty and extensinsibility
#               class Child(Parent)


class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f'{self.name} is eating')

  def sleep(self):
    print(f'{self.name} is sleeping')

  def kill(self):
    self.is_alive = False

  def describe(self):
    print(f'My name is {self.name}')
    print(f'Am I alive?: {self.is_alive}')

class Dog(Animal):
  def speak(self):
    print('WOOF')

class Cat(Animal):
  def speak(self):
    print('MEOW')

if __name__ == "__main__":
  juno = Cat("Juno")
  meme = Dog("Meme")

  juno.sleep()

  meme.sleep()

  juno.speak()

  juno.describe()

  juno.kill()

  juno.describe()