# Hangman in python
import random

_MAX_MISSES = 5
_BLANK_CHAR = "_"

def display_man(hangman_art, misses) -> None:
  man = hangman_art[misses]
  print("Hangman:")
  for str in man:
    print(str)

def game(word, blank, misses, hangman_art) -> None:
  guessed_letters = []

  while misses <= _MAX_MISSES and _BLANK_CHAR in blank:
    display_man(hangman_art, misses)
    print("Here is your word: ", end="")
    print(" ".join(blank))
    print()
    print(f"Guesses left: {6 - misses}")

    choice = input("Please enter in your guess: ")

    if not len(choice) >= 1 or not choice.isalpha():
      print("Please enter in a letter to guess.")
      continue
    if choice in guessed_letters:
      print(f"Already guessed '{choice}', pick another!")
      continue
    
    guessed_letters.append(choice)
    if choice in word:
      print("Correct guess!")
      
      for idx, char in enumerate(word):
        if choice == char:
          blank[idx] = char
    else:
      print("Wrong guess!")
      misses += 1
    print("---------------------------------------")

  if _BLANK_CHAR not in blank:
    print("Congragulations you won!")
    print(f"The word is: {word}")
  else:
    display_man(hangman_art, misses)
    print("You lost! :(")
    print(f"The word was: {word}")


if __name__ == "__main__":
  words = ("apple", "orange", "banana", "coconut", "pineapple")
  misses = 0
  hangman_art = {
    0 : ("  ",
        "   ",
        "   "),
    1 : (" o ",
        "   ",
        "   "),
    2 : (" o ",
        " | ",
        "   "),
    3 : (" o ",
        "/| ",
        "   "),
    4 : (" o ",
        "/|\\",
        "   "),
    5 : (" o ",
        "/|\\",
        "/  "),
    6 : (" o ",
        "/|\\",
        "/ \\"),
  }

  word = random.choice(words)
  blank = ["_"] * len(word)

  print("Welcome to Hangman.")
  game(word, blank, misses, hangman_art)
  

  # dictionary of key:()
