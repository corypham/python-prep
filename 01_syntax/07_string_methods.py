# usefule string methods



name = input("Enter you full name: ")

print("Your name is", len(name), "chars long.")

# find() returns first occurence of letter
char = input("Input a char you want to find in your name: ")
print("The char is at index ", name.find(char))

# rfind() returns last occurence of letter
char = input("Input a last char you want to find in your name: ")
print("The char is at index ", name.rfind(char))

# capitalize first letter
print(name.capitalize())

# make all letters upper case
print(name.upper())

# make all letters lower
print(name.lower())

# check if variable is int
print(name.isdigit())

# check if var has all letters
print(name.isalpha())

# count the number of chars within a string
print(name.count("c"))

# replace all chars with another
phone_number = input("Enter your phone number: ")
print(phone_number.replace("-", " "))

# to find all the string methods descriptions
print(help(str))

##################################################################
# username validator excercise 
##################################################################
def is_username():
  username = input("Enter in your username: ")   
  if len(username) > 12:
    print("Username is too long")
    return False
  elif not username.find(" ") == -1:
    print("Username cannot contain spaces.")
    return False
  elif not username.isalpha():
    print("Username cannot contain numbers")
    return False
  else:
    print(f"Welcome {username}")
    return True

def main():
  valid = is_username()
  if not valid:
    print("retry")
  else:
    print("congrats")

  return 0

if __name__ == "__main__":
  main()
