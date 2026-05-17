# Python Banking Program

# C++ is different from python where if a var is outer scope, you
# can read/write freely from an inner scope
# Python is differnt if you assign a var anywhere in function, python
# treats that as a local variable

total = 0
is_running = True

def display():
  print(f'Your total amount: ${total:.2f}')

def deposit():
  global total
  amount = float(input("Enter in amount to deposit: "))
  total += amount

def withdraw():
  global total
  while True:
    amount = float(input("Enter in amount to withdraw: "))
    if amount > total:
      print("Invalid entry. Cannot withdraw more than your total amount.")
      continue
    elif amount < 0:
      print("Amount must be greater than 0.")
      continue
    else:
      print(f'Succesfully withdrawed ${amount:.2f}')
      break

def main():
  global is_running
  while is_running:
    print("Banking Program (Enter in 1-4 options): ")
    print("1. Show your current balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter in your choice (1-4): "))

    match choice:
      case 1:
        display()
        continue
      case 2:
        deposit()
        continue
      case 3:
        withdraw()
      case 4:
        is_running = False
      case _: 
        print("Invalid Choice")

if __name__ == "__main__":
  main()