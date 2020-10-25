from hangman_draw import hangman
import random
# Hangman that will be shown when playing the game


# List of possible words to guess
words = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
#Word that the PC will choose randomly from the list words. We will have to guess this one.
choosen_word = random.choice(words)
print(choosen_word)

letter= input("Choose a letter: ")
print(f"Choosen letter = {letter}")

#check_letter = lambda x : print('Good job!') if (letter in choosen_word or letter in choosen_word.swapcase()) else print('Sorry, try again :(')

if (letter in choosen_word or letter in choosen_word.swapcase()):
    print('Good job!')
else:
    print('Sorry, try again :(')
print(hangman[5])