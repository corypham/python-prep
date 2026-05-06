# number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0


is_running = True


print("Python Number Guessing Game")
print(f'Select a number between {lowest_num} and {highest_num}')

while is_running:
  guess = input('Enter in your guess: ')

  if guess.isdigit():
    guess = int(guess)
    guesses += 1
  else:
    print(f'Invalid guess, please select a number beterween {lowest_num} and {highest_num}')
    continue

  if guess > answer:
    print('Your guess is higher than the answer.')
  elif guess < answer:
    print('Your guess is lower than the answer')
  else:
    print('Correct!')
    break
