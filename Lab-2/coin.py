"""Match Coins Game
   Rachel Remick
   9/27/2026"""

import random


class Coin:

    def __init__(self, heads_sideup, tails_sideup):
        self.heads_sideup = heads_sideup
        self.tails_sideup = tails_sideup

    def toss(self):
        number = random.randint(0, 1)
        if number == 0:
            self.sideup = self.heads_sideup
        else:
            self.sideup = self.tails_sideup

    def get_sideup(self):
        return self.sideup
