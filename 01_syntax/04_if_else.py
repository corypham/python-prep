#      Else do something else
# if = Do some code only IF some condition is True

age = int(input("Please enter an age: "))


if age >= 18:
  print("You are an adult!")
elif age < 0:
  print("You haven't been born yet")
else:
  print("You are not an adult")


response = str(input("Would you like some food? (Y/N): "))

if response == 'Y':
  print("Have some food")
else:
  print("No food for you")

for_sale = True

if for_sale:
  print("Item is for sale.")
else:
  print("Not for sale")

####################################################################
# Calculator Python
####################################################################

def calculator(operator, val1, val2):
  if operator == '-':
    return val1 - val2
  elif operator == '+':
    return val1 + val2
  elif operator == '*':
    return val1 * val2
  elif operator == '/':
    return val1 / val2
  else:
    return None


def main():
  operator = input("Enter an operator (- + * /): ")
  val1 = int(input("Enter in the first value: "))
  val2 = int(input("Enter in the second value: "))

  result = calculator(operator, val1, val2)
  if result:
    print(f"The result is: {result}")
  else:
    print("Invalid input.")
  return 0

if __name__ == "__main__":
  main()