import random

card_symbols = ["Clubs", "Diamonds", "Hearts", "Spades"]
card_values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

random_symbols = random.choice(card_symbols)
random_values = random.choice(card_values)

print(f"Random card is : {random_values} {random_symbols}")
