# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one conditions must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 25
is_raining = False
temp = 90
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
  print("Outdoor event is cancelled.")
elif temp >= 90 and is_sunny:
  print("Its too hot outside.")
elif not is_sunny:
  print("It is cloudy")
else:
  print("The outdoor event is still scheduled")