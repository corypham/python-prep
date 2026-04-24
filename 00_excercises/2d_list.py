fruits = ['apple', 'banana', 'coconut', 'orange']
vegetables = ['celery', 'carrots', 'potatoes']
meats      = ['chicken', 'fish', 'turkey', 'salmon']

groceries = [fruits, vegetables, meats]

print(groceries[0][2])

for i in range(len(groceries)):
  for j in range(len(groceries[i])):
    print(groceries[i][j], end=' ')
  print()

for collection in groceries:
  for food in collection:
    print(food, end=' ')
  print()


for grocery in groceries:
  print(grocery)