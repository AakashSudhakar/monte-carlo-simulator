"""
FILENAME:               main.py
AUTHOR:                 Aakash Sudhakar
DATE CREATED:           Monday, October 22, 2018
DATE LAST EDITED:       Monday, October 22, 2018
DESCRIPTION:            Main file containing logic for the Monte Carlo Python Simulation project
                        based off of the advanced Python project on pythonprogramming.net. 
"""

import math, random

def roll_dice():
    return random.randint(1, 100)

def main():
    x = 0
    while x < 100:
        result = roll_dice()
        print(result)
        x += 1

if __name__ == "__main__":
    main()