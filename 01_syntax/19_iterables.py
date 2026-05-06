#
# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop.
#

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
  print(num)
print()
for num in reversed(numbers):
  print(num)
print()

for i in range(len(numbers)):
  print(numbers[i])


print()
for i in range(len(numbers)-1, -1, -1):
  print(numbers[i])

names = {'kyla', 'jeremy', 'cory', 'michael'}
# ^ cannot iterate through a set because it is unordered


my_dict = {'A' : 1, 'B' : 2, 'C': 3}

for key, value in my_dict.items():
  print(f"{key} : {value}")

