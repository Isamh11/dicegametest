import random

class Dice:
    def __init__(self):
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

    def __str__(self):
        return str(self.value)