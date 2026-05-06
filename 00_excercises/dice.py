# dice program

import random


dict_dice = {
  1 : "*",
  2 : "**",
  3 : "***",
  4 : "** **",
  5 : "*** **",
  6 : "*** ***"
}

rolls = []

total = 0

num_dice = int(input("Enter in the number of dice to roll: "))

for dice in range(num_dice):
  rolls.append(random.randint(1, 6))
  total += rolls[dice]

  print(dict_dice.get(rolls[dice]))

print(total)
print(rolls)
