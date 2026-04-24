#
# Typecasting = the process of converting a variable from on data
#               type to another: str(), int(), float(), bool()

name = "Cory Pham"
age = 23
gpa = 3.6
is_engineer = True


print(f"Name {name} is type: ", type(name))
print(f"{age} is type: ", type(age))
print(f"{is_engineer} is type: ", type(is_engineer))

age = float(age)

print(f"{age} is type: ", type(age))

age = str(age)

print(f"{age} is type: ", type(age))

# Check if the string is empty or not
name = bool(name)
print(f"Name is {name}")
