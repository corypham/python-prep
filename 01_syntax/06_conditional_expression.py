# conditional expression = A one-line shortcut for the if-else statement
#                          (Ternary Operator). Print or assign of two values
#                          based on a condition.
#                          X is condiion else Y

num = 5

user_role = 'admin'

boss = True

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"

print(result)

access_level = "Full Acess" if user_role == 'admin' else "Limited Access"

print("You are the boss" if boss else "You are not the boss")