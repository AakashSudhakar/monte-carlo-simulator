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
        # print("\nRoll is {}.\n\nYOU LOSE.\n".format(roll))
        return False
    elif roll <= 50:
        # print("\nRoll is {}, which is inclusively between 1 and 50.\n\nYOU LOSE.\n".format(roll))
        return False
    else:
        # print("\nRoll is {}, which is inclusively between 51 and 99.\n\nYOU WIN!\n".format(roll))
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
        # print("\nCURRENT FUNDS: ${}\n".format(value))
    return value

def main():
    (funds, initial_wager, wager_count) = (10000, 100, 100)
    final_funds = simple_bettor(funds=funds, initial_wager=initial_wager, wager_count=wager_count)
    print("\nSTARTING FUNDS:  ${}\nFINAL FUNDS:  ${}".format(funds, final_funds))
    if final_funds > funds:
        print("\nAfter {} wagers, you won ${}.\n\nCONGRATULATIONS!\n".format(wager_count, final_funds - funds))
    elif final_funds == funds:
        print("\nAfter {} wagers, you didn't win or lose any money.\n\nINTERESTING...\n".format(wager_count))
    else:
        print("\nAfter {} wagers, you lost ${}.\n\nEPIC FAIL!\n".format(wager_count, funds - final_funds))

if __name__ == "__main__":
    main()