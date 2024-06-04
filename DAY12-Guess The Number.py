from random import randint

EASY_TURNS = 10
HARD_TURNS = 5


def check(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("This is higher. Guess a smaller number.")
    return turns - 1
  elif guess < answer:
    print("This is lower. Guess a larger number.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose difficulty level. Easy or hard: ").lower()
  if level == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS

def guessing_game():
  print("Welcome to the Number Guessing Game! You have to guess a number!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  

  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose. The correct number was:",answer)
      return
    elif guess != answer:
      print("Guess again.")


guessing_game()

