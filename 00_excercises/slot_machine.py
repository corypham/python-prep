# slot machine program
import random
import time

def roll() -> list[str]:
  symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
  combo = []

  for i in range(3):
    combo.append(random.choice(symbols))
  return combo

def print_row(combo) -> None:
  print("Roll: ", end="")
  print(*combo, sep=" | ")
  return None

def get_payout(balance):
  print(f"Current balance: ${balance:.2f}")
  return None

def handle_roll(balance) -> int:

  while True:
    bet = input("Enter in amount to bet: ")
    if not bet.isdigit() or int(bet) > balance or int(bet) < 0:
      print(f"Invalid selection. Please enter in bet that is a number or less than your remaining balance (${balance:.2f})")
      continue
    else:
      print("Spinning...")
      combo = roll()
      for symbol in combo:
        time.sleep(1)
        print(symbol, end='|', flush=True)
      print()
      if combo[0] == combo[1] == combo[2]:
        balance += int(bet) * 2
        print(f"You won ${int(bet) * 2:.2f}!")
        get_payout(balance)
        break
      else:
        balance -= int(bet)
        print(f"You lost ${int(bet):.2f}.")
        get_payout(balance)
        break

  return balance

def main():
  balance = 100
  is_running = True

  print("*******************************")
  print("Welcome to Python Slots")
  print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
  print("*******************************")

  while is_running:
    print("*******************************")
    print("Select an option (1-3) below:")
    print("1) Quit")
    print("2) Get balance")
    print("3) Roll")
    print("*******************************")

    if balance <= 0:
      print("Insufficient funds :[")
      print("Exiting...")
      break
    get_payout(balance)
    print("*******************************")
    choice = input("Enter your selection: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
      print("Invalid selection. Please enter in digit 1-3.")
      continue
    else:
      choice = int(choice)
      match choice:
        case 1:
          print("Goodbye!")
          break
        case 2:
          get_payout(balance)
        case 3:
          balance = handle_roll(balance)

if __name__ == '__main__':
  main()
