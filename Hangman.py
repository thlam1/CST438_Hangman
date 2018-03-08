#Thomas Lam - CST 438
#Hangman game

import random


class HangmanGame(object):

    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |']
    man[2] = [' 0   |', ' |   |']
    man[3] = [' 0   |', '/|   |']
    man[4] = [' 0   |', '/|\\  |']
    man[5] = [' 0   |', '/|\\  |', '/    |']
    man[6] = [' 0   |', '/|\\  |', '/ \\  |']

    pics = []

    words = '''computer'''.split()

    infStr = '---------------------------------------------------------------'

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)

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

    def info(self, info):
        ln = len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])

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
                print('You\'ve already tried this letter.')
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