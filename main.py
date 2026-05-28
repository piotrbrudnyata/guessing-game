import random
from range import Number

class User:
    def get_input(self):
        return input("Guess the number: ")

class Game:
    def __init__(self):
        self.number = Number()
        self.user = User()
        self.score = 10

    def process_guess(self, guess):
        if guess == "exit":
            print("Game ended")
            return False

        if guess == "is the number even":
            if self.number.is_even():
                print("The number is even")
            else:
                print("The number is odd")
            return True

        if guess.isdigit() and int(guess) == self.number.value:
            print("You won!")
            print(f"Your score: {self.score}")
            return False

        print("Wrong guess")
        self.score -= 1
        return True

    def start(self):
        print("The game is started")

        running = True
        while running and self.score > 0:
            guess = self.user.get_input()
            running = self.process_guess(guess)

        if self.score <= 0:
            print("You lost! Score is 0.")


if __name__ == "__main__":
    Game().start()