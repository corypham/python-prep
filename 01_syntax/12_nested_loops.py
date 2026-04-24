# nested loops = A loop within another loops (inner, outer)
#                outer loop:
#                   inner loop:

# print on the same line
for x in range(3):
  for y in range(1, 11):
    print(y, end=" ")
  print()

#################################################################
# Table excercise
#################################################################

def table():
  rows = int(input("Enter the number of rows: "))
  cols = int(input("Enter the number of columns: "))
  symbol = input("Enter in a symbol to use: ")

  for outer in range(rows):
    for inner in range(cols):
      print(symbol, end="")
    print()
  
  return None

def main():
  table()
  return 0


if __name__ == "__main__":
  main()