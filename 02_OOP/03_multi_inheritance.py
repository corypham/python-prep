# multiple inheritance = child inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another
#                          C(B) <- B(A) <- A


class Animal:
  def __init__(self, name) -> None:
    self.name = name
    self.is_alive = True
  
  def eat(self) -> None:
    print('Im eating')

  def kill(self) -> None:
    self.is_alive = False
    print(f'Killed {self.name}')

  def describe(self) -> None:
    print(f'My name is {self.name}')
    if self.is_alive:
      print('I am alive')
    else:
      print('I am dead')

class Prey(Animal):
  def flee(self):
    print(f"This {self.name} is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f'This {self.name} is hunting')

class Rabbit(Prey):
  def jump(self) -> None:
    print(f'{self.name} jumping')

class Hawk(Predator):
  def squeek(self) -> None:
    print('{self.name} squeeking')

# Fish class can be both prey + predator, so it inherits both classes
# just add aditional class to inheritance list parameter
class Fish(Prey, Predator):
  pass

if __name__ == '__main__':
  rabbit = Rabbit("hare")
  hawk = Hawk('Eagle')
  fish = Fish('Salmon')
  prey = Prey('bitch')
  
  prey.flee()
  hawk.hunt()
  fish.hunt()
  fish.flee()

  fish.describe()

  fish.kill()

  fish.describe()

