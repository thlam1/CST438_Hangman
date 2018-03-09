#Thomas Lam - CST 438
#Hangman game

import random
import string


class HangmanGame(object):

#this builds the hangman noose and stand
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

#this builds via increment array the man
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |']
    man[2] = [' 0   |', ' |   |']
    man[3] = [' 0   |', '/|   |']
    man[4] = [' 0   |', '/|\\  |']
    man[5] = [' 0   |', '/|\\  |', '/    |']
    man[6] = [' 0   |', '/|\\  |', '/ \\  |']

    pics = []

    #opens the given class text file with all the word options
    f = open("hangmanwords.txt")
    text = f.read()
    words = text.split()

    #break line at the end of the game
    breakStr = '-----------------------------------------------------'

    #initialize
    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    #pick the word to use from text file
    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    #prints the next line to display visual hangman progress & state
    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)

    #error check user input
    def askAndEvaluate(self, word, result, missed):
        guess = input()
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    #break string at the end for separation
    def info(self, info):
        ln = len(self.breakStr)
        print(self.breakStr[:-3])
        print(info)
        print(self.breakStr[3:])

    #program Hangman start
    def start(self):
        print('Welcome to CST 438 - Hangman!')
        word = list(self.pickWord())
        result = list('*' * len(word))
        print('The word is: ', result)
        state, i, missed = False, 0, []
        while i < len(self.pics) - 1:
            print('Guess the word: ', end='')
            guess, right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('Invalid input. Try again!')
                continue
            print(''.join(result))
            if result == word:
                self.info('YOU WIN! CONGRATULATIONS')
                state = True
                break
            if not right:
                missed.append(guess)
                i += 1
            self.printPic(i, len(word))
            print('Missed characters: ', missed)

        if not state:
            self.info('YOU RAN OUT OF GUESSES AND LOST!')



a = HangmanGame().start()