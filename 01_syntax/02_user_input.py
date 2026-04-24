# input() = A function that prompts the user to enter data
#           Return the entered data as a string.


name = input("What is your name?: ")

# Need to typecast age in order to increment
age = int(input("What is your age?: "))

print(f"Hello {name}")
print(f"{name} is data type ", type(name))

print("Happy Birthday!")
age += 1


print(f"You are {age} years old.")

