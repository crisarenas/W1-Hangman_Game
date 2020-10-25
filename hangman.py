## Import hangman draw from another python file
from hangman_draw import hangman
import random

# List of possible words to guess
words = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")

#Word that the PC will choose randomly from the list words. We will have to guess this one.
choosen_word = random.choice(words)
print(choosen_word)

# Functions that will be used
count = 0
def choose(count):
    ''' User interation. Choose a letter and check if it is OK.'''
    letter= input("Choose a letter: ")
    if (letter in choosen_word or letter in choosen_word.swapcase()):
        print('Good job!')
        print(hangman[count])
        
    else:
        print('Sorry, try again :(')
        count += 1
        print(hangman[count])
    return count

#while user_word != choosen_word:


for i in range(8):
    count = choose(count)

'''
def letter_in_word():
    print('Good job!')
    print(hangman[count])


def letter_not_in_word():
    print('Sorry, try again :(')
    count += 1
    return count
'''