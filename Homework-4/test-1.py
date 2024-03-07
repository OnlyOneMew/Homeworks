import random

input_players = input("How many players are playing the game?: ")

if input_players.isdigit() and int(input_players) > 0:
    num_players = int(input_players)

    for player in range(1, num_players + 1):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"Player {player}: Dice: {dice_1} {dice_2}")

    print("Program finished.")
else:
    print("Please enter a positive integer")
