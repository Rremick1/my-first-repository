"""Match Coins Game
   Rachel Remick
   9/27/2026"""

import random


class Coin:

    def __init__(self, sideup):

        self.__sideup = sideup


    def toss(self):
        number = random.randint(0, 1)
        if (number == 1):
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
