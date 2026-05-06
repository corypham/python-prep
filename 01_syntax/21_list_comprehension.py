# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
#

doubles = []

for x in range(1, 11):
  doubles.append(x * 2)

print(doubles)


# you can compact this code
doubles = [x*2 for x in range(1, 11)]
print(doubles)

names = ['cory', 'kyla', 'jeremy', 'scott']

upper_case = [name[0].upper() for name in names]
print(upper_case)

# with a condition
numbers = [1, -2, -4, 0, 10, 4]

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)