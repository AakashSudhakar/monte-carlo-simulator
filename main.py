"""
FILENAME:               main.py
AUTHOR:                 Aakash Sudhakar
DATE CREATED:           Monday, October 22, 2018
DATE LAST EDITED:       Tuesday, October 23, 2018
DESCRIPTION:            Main file containing logic for the Monte Carlo Python Simulation project
                        based off of the advanced Python project on pythonprogramming.net. 
"""

import math, random

def roll_dice():
    roll = random.randint(1, 100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True

def simple_bettor(funds, initial_wager, wager_count):
    """
    Main function to receive static monetary quantity and run simple betting algorithm. 
    """
    value, wager, current_wager = funds, initial_wager, 0
    while current_wager < wager_count:
        if roll_dice() is True:
            value += wager
        else:
            value -= wager
        current_wager += 1
    if value <= 0:
        value = "BROKE"
    print("\nCURRENT FUNDS: ${}\n".format(value))

def main():
    (funds, initial_wager, wager_count), x = (10000, 100, 50), 0
    while x < 100:
        simple_bettor(funds=funds, initial_wager=initial_wager, wager_count=wager_count)
        x += 1

if __name__ == "__main__":
    main()