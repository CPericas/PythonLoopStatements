# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to 
# select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
import random

items = ['magic wand', 'health potion', 'sword', 'invisibility cloak']

random_pick = random.choice(items)
choice = input("Choose one of the following: magic wand, health potion, sword, or invisibility cloak: ")

if random_pick == choice:
    print("Congratulations! You picked correctly!")
else:
    print(f"I'm sorry, that is incorrect. The correct choice was {random_pick}.")