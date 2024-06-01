#This code contains art of hammer and clear() function from Replit Library.
#The link for art of hammer: https://replit.com/@devmoh04/blind-auction-start#art.py


from replit import clear
from art import logo

print(
    "Welcoe to the BIDDING PROCESS! Today we are going to bid for MAJNU BHAI KA GHODA !!"
)
print(logo)

bids = {}
finished = False


def winner(record):
  highest_bid = 0
  winner = ""
  for bidder in record:
    bid_amt = record[bidder]
    if bid_amt > highest_bid:
      highest_bid = bid_amt
      winner = bidder
  print(
      f"The winner of this Bid is {winner} with a bid of ${highest_bid}.\n CONGRATULATIONS {winner}!!!"
  )


while not finished:

  name = input("Enter your name: ")
  player_bid = int(input("What is your Bid? $"))

  bids[name] = player_bid
  a = input("Any other bidders remaining? Y/N?: ").lower()
  if a == "y":
    clear()
  elif a == "n":
    finished = True
    winner(bids)
  else:
    print("enter correctly")
