# class variables = Shared among all instances of a class 
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from
#                   that class

# Student class object is created in memory and shared among all instances
# of this class. Reference by using the keyword of the class itself.
class Student:

  # place class variable outside of constructor for each object to share.
  class_year = 2024
  num_students = 0

  def __init__(self, name, age = 67) -> None:
    self.name = name
    self.age = age
    Student.num_students += 1

  def describe(self):
    print(f'{self.name}')
    print(f'{self.age}')
    print(f'{Student.class_year}')
    print(f'{Student.num_students}')



if __name__ == "__main__":
  student1 = Student("Spongebob", 30)
  student2 = Student("Patrick", 35)
  student3 = Student("Sandy", 67)
  student4 = Student("Cory")

  student1.describe()

  # instance state vs shared class state
  print(f'{Student.num_students}')
