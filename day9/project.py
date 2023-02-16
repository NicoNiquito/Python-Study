from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
bidders_list = {}
should_end = False

def bidder_winner(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not should_end:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bidders_list[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    should_end = True
    bidder_winner(bidders_list)
  elif should_continue == "yes":
    clear()
