import random

class NumberGuessingGame:
    def __init__(self, rng, input, print):
        self.rng = rng
        self.input = input
        self.print = print
        self.secret = self.rng(1, 100)

    def main(self):
        while True:
            guess = int(self.input("Guess a number: "))
            if guess < self.secret:
                self.print("too small. try again")
            elif guess > self.secret:
                self.print("too large. try again")
            else:
                self.print("Bravo! That's the one")
                break

if __name__ == "__main__":
    game = NumberGuessingGame(random.randint, input, print)
    game.main()



