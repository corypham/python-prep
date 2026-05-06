# random is a submodule that contains helpful functions that
# generate random integers

import random

# randomly generate a num 1 - 6
print(random.randint(1, 6))


low = 1
high = 100

print(random.randint(low, high))


# random floating point (0-1)
print(random.random())

# shuffle through a collection
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J']
random.shuffle(cards)
print(cards)

# randomly pick an option
options = ('rock', 'paper', 'scissors')
print(random.choice(options))
