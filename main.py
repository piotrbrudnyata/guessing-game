import random


class Number:
    def __init__(self):
        self.value = random.randint(1, 99)

    def is_even(self):
        return self.value % 2 == 0


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 10

    def decrease_score(self):
        self.score -= 1


class Result:
    @staticmethod
    def win(player):
        print("You won!")
        print(f"Your score: {player.score}")

    @staticmethod
    def lose():
        print("You lose!")

    @staticmethod
    def even():
        print("The number is even.")

    @staticmethod
    def odd():
        print("The number is odd.")


class Game:
    def __init__(self):
        self.player = Player("User")
        self.number = Number()

    def start(self):
        print("The game is started")

        while True:
            answer = input("Guess the number: ")

            if answer.lower() == "exit":
                print("Game ended.")
                break
            
            elif answer.lower() == "is the number even":
                if self.number.is_even():
                    Result.even()
                else:
                    Result.odd()

            else:
                # Check if input is a number
                if not answer.isdigit():
                    print("Please enter a valid number.")
                    continue

                user_number = int(answer)

                if user_number == self.number.value:
                    Result.win(self.player)
                    break
                else:
                    Result.lose()
                    self.player.decrease_score()

                # Optional: game over if score reaches 0
                if self.player.score == 0:
                    print("Game over! Your score reached 0.")
                    print(f"The correct number was {self.number.value}")
                    break


# Run the game
game = Game()
game.start()

    

    # TODO: Features 
    # use loop
    # take input for finishing the game
    # take input for hint question 
    # add scoring mechanism 

    # TODO: Refactor
    # extract classes
    # use separate files




