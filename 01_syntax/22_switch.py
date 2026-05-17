#
# Match-case statement (switch): An alternative to using many 'elif' 
#                                statements. Execute some code if a value
#                                matches a 'case'
# Benefits: cleaner and syntax is more readable


def day_of_week(day):
  if day == 1:
    return "it is sunday"
  elif day == 2:
    return "it is monday"
  else:
    return "your gay"
  
def match_case(day):
  match day:
    case 1:
      return "it is sunday"
    case 2 | 3 | 4 | 5 | 6 | 7:
      return "it is monday"
    case _:
      return "your gay"
  
print(day_of_week(1))