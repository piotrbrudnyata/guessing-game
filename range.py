import random

class Number:
    def __init__(self):
        self.value = random.randint(1, 99)

    def is_even(self):
        return self.value % 2 == 0
