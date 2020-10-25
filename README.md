# Hangman Game


## Creating a hangman
The first thing that I tried when creating a hangman was doing it with a string. However, as seen in the picture below, it can be pretty frustrating when working with so many spaces.

![](hangman_nocomments.jpg)

That's when I discovered that a comment can be assigned to a variable. This made everything much simplier.

``` python
  hangman = ['''
     ____
    |    |
    |    O
    |   /|\
    |   / \
  __|__      '''] 
```
So, to print the hangman, we will use:
 * ``` hangman[0]```: pole.
 * ``` hangman[1]```: pole + head.
 * ``` hangman[2]```: pole + head + torso.
 * ``` hangman[3]```: pole + head + torso + 1 arm.
 * ``` hangman[4]```: pole + head + torso + 2 arms.
 * ``` hangman[5]```: pole + head + torso + 2 arms + 1 leg.
 * ``` hangman[6]```: dead.

## Problems
* Installinh ```pip install Random-Word-Generator``` to generate random words using a library.
    * Error :  ``` No module named ...```

