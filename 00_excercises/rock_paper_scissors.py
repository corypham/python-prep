import random



options = ('rock', 'paper', 'scissors')

# use a list of tuples to store winning combos
wins = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

choice = None
is_running = True

while is_running:
  computer = random.choice(options)
  print('Enter "q" to quit')
  choice = input('Enter in your choice (rock, paper, scissors): ')
  

  if choice == 'q':
    break
  elif choice not in options:
    print('Invalid choice, please select (rock, papers, scissors)')
    continue

  print(f'Computer Choice: {computer}')
  print(f'Your Choice: {choice}')

  if (choice, computer) in wins:
    print("You win!")
  elif choice == computer:
    print("That was a tie.")
  else:
    print('You lost! :(')
  

