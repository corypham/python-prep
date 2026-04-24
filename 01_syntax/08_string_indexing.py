# indexing = accessing elements of a sequence using[] (indexing operator)
#            [start : end : step]


# If you dont want characters to be prefaced by \ to be intepreted 
# as a special character, you can use raw strings by adding r before the first quote

print(r"C:\this\name")

# Strings can be concatenated with + operator and repeated with *
print(3 * 'un' + 'ium')

prefix = 'Py'
print (prefix + 'thon')

# Strings can be indexed 
word = "Python"
print (word[0])
print(word[-5])

# Slicing is also supported, allows you to obtain a substring
print(word[0:2])
print(word[:4] + word[4:])

# print every second character
credit_number = "1234-5678-91011"
print(credit_number[::2])

# print the last 4 chars
last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

# Python strings cannot be changed, they are immutable

# use built in len() function that returns the length of a string
print(len(prefix))