# while loop = execute some code WHILE some condition remains true 


age = int(input("Enter in your age: "))

while (age < 18):
  print("You are not an adult.")
  age = int(input("Enter in your age again: "))

print(f"Your age is {age}")

food = input("Enter a food you like (q to quit): ")

while not food == 'q':
  print(f"You like {food}")
  food = input('Enter another food you like (q to quit): ')

max = int(input("Enter in a maxber to print up to: "))
num = 0

while True:
  print(f"number: {num}")
  num +=1

  if num >= max:
    break

print("bye")