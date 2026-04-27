# Concession stand program

menu = {
  'pizza' : 3.00,
  'nachos' : 4.50,
  'popcorn' : 5.20,
  'pretzels' : 8.67,
  'hotdog' : 11.00,
  'beer' : 8.99
}

cart = []

total = 0

while True:
  food = input("Enter item to add to cart (press q to quit): ").lower()

  if food == 'q':
    break
  elif food is not None and menu.get(food) is not None:
    cart.append(food)
  else:
    print('Invalid selection, please select from cart.')

  print('--------- MENU ----------')
  for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')
  print('-------------------------')


for item in cart:
  total += menu[item]

print(f'Your total: {total}')
