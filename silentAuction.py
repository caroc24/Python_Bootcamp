bid_dictionary = {}

name = ""
bid = 0

more_bidders = True

while more_bidders == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dictionary[name] = bid
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if yes_or_no == "no":
        more_bidders = False
    else:
        print("\n" * 20)

highest_bid = 0
highest_bidder = ""

for key in bid_dictionary:
    if bid_dictionary[key] > highest_bid:
        highest_bid = bid_dictionary[key]
        highest_bidder = key

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")