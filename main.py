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
        print("\nRoll is {}.\n\nYOU LOSE.\n".format(roll))
        return False
    elif roll <= 50:
        print("\nRoll is {}, which is inclusively between 1 and 50.\n\nYOU LOSE.\n".format(roll))
        return False
    else:
        print("\nRoll is {}, which is inclusively between 51 and 99.\n\nYOU WIN!\n".format(roll))
        return True

def main():
    x = 0
    while x < 100:
        result = roll_dice()
        print(result)
        x += 1

if __name__ == "__main__":
    main()