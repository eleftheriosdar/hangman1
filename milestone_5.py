import random


class Hangman():
    def __init__(self, word_list, num_lives):
        #word_list: a list of possible words to be guessed
        self.word_list = word_list
        #num_lives the lives for the user to play and guess
        self.num_lives = num_lives
        #word is the random selected word for the word_list
        self.word = list(random.choice(self.word_list))
        #list_of_guessses a list of guesses that have already been tried initilised into an empty list
        self.list_of_guesses=[]
        #word_guessed is a list of the words that are corrcet
        self.word_guessed = ['_']*len(self.word)
        #num_letters is the number of unique letters that have not been guessed yet
        self.num_letters= len(set(self.word))
        
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in list(self.word):
            print("Good guess!  {} is in the word".format(guess))
            for index, letter in enumerate(self.word):
                #TODO I need to use a different operator because guess is not going to be equal to the guessing word
                if letter in guess:
                    self.word_guessed[index] = letter
                self.num_letters -=1
        print("Yes letter {} is in the word".format(guess))
        print("Your word so far : {} ".format(self.word_guessed))
  
        else:
            self.num_lives -=1
            print("Sorry, {}  is not in the word, Try again!".format(guess))
            print("You have {} lives left".format(self.num_lives))
        
    

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter  ").lower()
            if (len(guess) != 1) and (guess.isalpha() == False):
                print("Invalid letter. Please, enter a single alphabetical character.  ")
            elif guess in self.list_of_guesses:
                print("Your already tried that letter")
                guess = input("Enter a single letter   ")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
            
    def play_game(self, word_list):
        self.game = Hangman(word_list, num_lives=5)
        



hangman = Hangman(["banana"])
hangman.ask_for_input()
