# Membership operators = used to test whether a value or variable is found in
#                        a sequence (list, string, tuple, set, dict)
#                        Returns a boolean
# 1. in
# 2. not in


word = "APPLE"

letter = input("Enter in letter: ")

if letter not in word:
  print("You guessed correctly")
else:
  print("You guessed incorrectly") 


grades = {"Sandy" : "A",
          "Squidward" : "B",
          "Spongebob" : "C",
          "Patrick" : "F"}

student = input("Enter in the name of a student: ")

# iterating through dict returns a boolean
if student in grades:
  print(f'{student}s grade is {grades[student]}')
else:
  print(f'{student} not found')


email = 'corypham@gmail.com'

if '@' in email and '.' in email:
  print('Valid email')
else:
  print('valid email')