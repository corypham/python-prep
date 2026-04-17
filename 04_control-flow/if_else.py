# if statements

x = int(input("Please enter an integer: "))

if x % 3 == 0:
    print("Your number is divisible by 3.")
elif x % 3 == 1:
    print("Your number has a remainder of 1 when divided by 3")
else:
    print("Your number has a remainder of 2 when divided by 3")