#This code conatins logo of blackjack game.
#goto: https://replit.com/@devmoh04/blackjack-final#art.py to import logo module
import random
from replit import clear
from art import logo

def deal():
  """gives a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You scored over 21. You LOOSE!!"


  if user_score == computer_score:
    return "It's a DRAW!!"
  elif computer_score == 0:
    return "You LOOSE, opponent has BLACKJCK!! "
  elif user_score == 0:
    return "You WIN with a BLACKJACK!!"
  elif user_score > 21:
    return "You scored over 21. You LOOSE!!"
  elif computer_score > 21:
    return "Opponent scored over 21. You WIN!!"
  elif user_score > computer_score:
    return "You WIN!!"
  else:
    return "You LOOSE!!"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for i in range(2):
    user_cards.append(deal())
    computer_cards.append(deal())

  while not game_over:
    user_score = score(user_cards)
    computer_score = score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal())
      else:
        game_over = True
        
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal())
    computer_score = score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
