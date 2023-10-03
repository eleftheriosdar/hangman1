import random

word_list = ["banana", "apple", "grapes", "cherries", "orange"]
word = random.choice(word_list)
print(word)



def ask_for_input ():
    guess = input("Enter a single letter  ")
    check_guess(guess)
    while True:
        if (len(guess) == 1) and (guess.isalpha() == True):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.  ")
            guess = input("Enter a single letter  ")
            


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess!  {} is in the word".format(guess))
        return guess
    else:
        print("Sorry, {}  is not in the word, Try again!".format(guess))
        return guess


ask_for_input()
