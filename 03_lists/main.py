
"""
A python list is a highly flexible data structure that can store elements
of different data types (heterogeneous). It is a dynamic array that automatically
resizes as items are added or removed. Slightly different from a C++ vector
where a vector forces every elements to be of the same data type and stores
actual values directly in memory.

It can store a mix of data types because it actually stores a continious 
array of pointers (references) to objects, rather than the objects themselves
"""

squares = [1, 4, 9, 16, 25]
print(squares)

# You can slice lists like strings
squares[-3:]

# supports concatenation
print(squares + [36, 49])

# you can add new items to the end of the list
squares.append(9 ** 2)
print(squares)

# Simple assignment in python never copies data. When you assign a list to a
# variable, the variable points to the existing list
rgb = ["Red", "Blue", "Green"]
rgba = rgb
print(id(rgb) == id(rgba))
rgb.append("Alpha")
print(rgba)

# Slice assignment is possible
letters = ['a', 'b', 'c', 'd', 'e', 'f','g' ]
print(len(letters))
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:6] = []
print(letters)
letters[:] = []
print(letters)

# Nest lists within a list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[1][2])