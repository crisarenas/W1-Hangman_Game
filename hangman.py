## Import hangman draw from another python file
from hangman_draw import hangman
import random

# List of possible words to guess
words = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")

#Word that the PC will choose randomly from the list words. We will have to guess this one.
choosen_word = random.choice(words)
print(choosen_word)

# Genero un string de la forma _ _ _ _ que coincida con el numero de caracteres de la palabra
current_word = []
for _ in choosen_word:
    current_word.append("_")
print(' '.join(current_word))


# Functions that will be used
def choose(count):
    ''' User interation. Choose a letter and check if it is OK.'''
    letter= input("Choose a letter: ")
    
    already_said = ''
    already_said += letter
    if (letter in choosen_word or letter in choosen_word.swapcase()):
        print('Good job!')
        print(hangman[count])
        coincidencia = []
        for c in choosen_word:
            if c == letter:
                coincidencia.append(choosen_word.index(c))
        
        for index in coincidencia:
            current_word[index] = letter
        print(' '.join(current_word))
        
    else:
        print('Not in word, try again.')
        count += 1
        print(hangman[count])
    print(f'\nLetters that you have already tried : {already_said} \n------------------------------------')
        
    return count




count = 0
# Mientras que no llegemos a mostrar el muñeco completp
while count < 7:
    if''.join(current_word) != choosen_word:
        count = choose(count)
    else:
        print('You won!')
    
    
'''
def letter_in_word():
    print('Good job!')
    print(hangman[count])


def letter_not_in_word():
    print('Sorry, try again :(')
    count += 1
    return count

def check_letter():
    while letter not in ascii_letters:
        letter= input("make sure it is a letter: ")
'''