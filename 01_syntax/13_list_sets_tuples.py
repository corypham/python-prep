#
# collection = a single variable used to store multiple values
#    List  = [] ordered and changeable. Duplicates are OK
#    Set   = {} unordered and immutable, but Add/Remove are OK. NO duplicates
#    Tuple = () ordered and unchangeable. Duplicates are Ok. FASTER 

##################################################################
# Lists
##################################################################

"""
A python list is a highly flexible data structure that can store elements
of different data types (heterogeneous). It is a dynamic array that automatically
resizes as items are added or removed. Slightly different from a C++ vector
where a vector forces every elements to be of the same data type and stores
actual values directly in memory.

It can store a mix of data types because it actually stores a continious 
array of pointers (references) to objects, rather than the objects themselves
"""

# USE: when collection expected to grow and shrink or need to sort

squares = [1, 4, 9, 16, 25]
print(squares)

# can always use the print help() function to see the methods avail
# print(help(squares))
print(len(squares))
print(9 in squares)

# You can slice lists like strings
print(squares[-3:])

# supports concatenation
print(squares + [36, 49])

# you can add new items to the end of the list
squares.append(9 ** 2)
print(squares)

for square in squares:
  print(square, end=' ')

# Simple assignment in python never copies data. When you assign a list to a
# variable, the variable points to the existing list
rgb = ["Red", "Blue", "Green"]
rgba = rgb
print(id(rgb) == id(rgba))
rgb.append("Alpha")
print(rgba)
rgb.remove("Red")
print(rgb)
rgb.insert(0, "White")
rgb.sort()
print(rgb)
rgb.reverse()
print(rgb)
print(rgb.index("Alpha"))
print(rgb.count("Green"))
rgb.clear()

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


##################################################################
# Sets
##################################################################

# they are essentially equivalent to unordered_set in C++
# cannot index a set because it is unordered
# automatically remove duplicate values
# mutable, you can add or remove them but elements themselves are not
# Optimized for membership checking O(1)
# USE: ensure all items are unique

fruits = {"apple", "orange", "banana", "cocounut"}
print(len(fruits))
print("apple" in fruits)

fruits.add("pineapple")
fruits.remove("apple")
for fruit in fruits:
  print(fruit, end=' ')
print()
fruits.pop()
print(fruits)
fruits.clear()

##################################################################
# Tuples
##################################################################
# Immutable: elements cannot be modified once defined
# faster and more memory efficient due to fixed size
# few methods (primarily count and index)
# ordered and allows duplicates
# USE: fixed collection of related items that cannot be changed

names = ('Cory', 'Jeremy', 'Kyla', 'Chloe', 'Cory')

for name in names:
  print(name, end=' ')

print(names.index('Kyla'))

# you can also use the enumerate() function on a collection that holds
# tuples. In each tuple object, must be pair/two values for tuple unpacking

array = ['cory', 'kyla', 'jeremy', 'michael', 'ethan']

for index, name in enumerate(array, 1):
  print(f'{index:2} {name}')

