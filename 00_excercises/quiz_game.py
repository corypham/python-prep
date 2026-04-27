# Python quiz game

questions = (("How many goons do I do"),
             ("What is my middle name"),
             ("Who is my favorite basketball player"),
             ("Who is donald trump"),
             ("Where was my first goon"),
             ("Who are you"))

options = (("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."),
           ("A.", "B.", "C.", "D."),
           ("A.", "B.", "C.", "D."))

answers = ("C", "B", "A", "D", "C", "A")

guesses = []

score = 0

questions_num = 0

for question in questions:
  print('----------------')
  print(question)
  for option in options[questions_num]:
    print(option)
    print()
  guess = input("Enter your guess: ").upper()

  guesses.append(guess.upper())

  if guess == answers[questions_num]:
    score += 1
  else:
    print("Incorrect!")
    print(f"{answers[questions_num]} is the correct answer.")

  questions_num += 1

print('----------------')
print('Your score is: ', score / len(questions_num))
print('----------------')



print('----------------')
print('YOUR RESULTS')
print('----------------')

for i in range(questions_num):
  print(f'Question {i + 1}.')
  print(f'{questions[i]}?')
  print(f'You answered: {guesses[i]}')
  print(f'Correct answer is: {answers[i]}')
  print('----------------')
