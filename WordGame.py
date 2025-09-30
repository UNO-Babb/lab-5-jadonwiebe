#Word Game is a knock-off version of a popular online word-guessing game.

import random


def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for char in word:
        if letter == char:
            return True 
        else:
            return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    CorrectLetter = word[spot]
    if letter == CorrectLetter:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    response = ""
    for unknown in range(5):
        MyLetter = myGuess[unknown]
        if inSpot(MyLetter, word, unknown) == True:
            response = response + MyLetter.upper()
        elif inWord(MyLetter, word) == True:
            response = response + MyLetter.lower()
        else:
            response = response + "_"
    return response

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess

    #Ask user for their guess
    guess = 1
    while guess <= 6:
        validWord = False
        while validWord == False:
            myGuess = input("Name a five letter word: ")
            myGuess = myGuess.lower()
            if myGuess not in wordList:
                print("That word is not in the list")
            else:
                validWord = True
  #Give feedback using on their word:
        response = rateGuess(myGuess, todayWord)
        print(response)
        if response == todayWord.upper():
            print("You got the right word in " + str(guess) + " tries!")
            guess = guess + 6
            win = True
        guess = guess + 1

    print("The correct word was", todayWord)

    print("Have a great day")



if __name__ == '__main__':
  main()
