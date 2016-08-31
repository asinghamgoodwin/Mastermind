import random

class Mastermind():
    def __init__(self):
        self.colorList = {"R": "Red", "B": "Blue", "G": "Green",
                "Y": "Yellow", "P": "Purple", "O": "Orange"}
        self.colorListValues = list(self.colorList.values())
        self.secretCode = self.makeSecretCode()
        self.guessHistory = []

    def makeSecretCode(self):
        secretCode = []
        for i in range(4):
            index = random.randint(0,5)
            secretCode.append(self.colorListValues[index])
        return secretCode

    def makeRandomGuess(self):
        randomGuess = []
        for i in range(4):
            index = random.randint(0,5)
            randomGuess.append(self.colorListValues[index])
        return randomGuess

    def run(self, wrong, right, guess):
        for i in range(right):
            pass
        #wrong, right = checkGuess()
        #while 

    def conversion(self, userGuess):
        niceGuess = []
        for c in userGuess:
            niceGuess.append(self.colorList[c])
        return niceGuess

    def checkGuess(self, guess):
        # checking right spot
        right_spot = 0
        for i in range(4):
            if guess[i] == self.secretCode[i]:
                right_spot += 1
        wrong_spot = 0
        # checking right colors
        for color in self.colorListValues:

            count_in_code = self.secretCode.count(color)
            count_in_guess = guess.count(color)
#            print(color)
#            print(count_in_code)
#            print(count_in_guess)
            wrong_spot += min(count_in_guess, count_in_code)
        wrong_spot -= right_spot
        self.guessHistory.append((guess, (wrong_spot, right_spot)))
        return wrong_spot, right_spot


if __name__ == "__main__":
    m = Mastermind()
    # m.secretCode = ["Red", "Orange", "Green", "Yellow"]
    # print("secret code:")
    # print(m.secretCode)
    max_guesses = 10
    for i in range(max_guesses):
        guess = list(input())
       # print(guess)
        nice = m.conversion(guess)
       # print(nice)
        check = m.checkGuess(nice)
        print(check)
        if check == (0,4):
            print("You won!!!!!")
            break
    print(m.guessHistory)
#    print(m.checkGuess(['Orange', 'Blue', 'Blue', 'Yellow']))











