import random

class Hangman:
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    list_of_guesses = []
    word = random.choice(word_list)
    word_guessed = ['_', '_', '_', '_', '_']
    num_letters = int()
    num_lives = 5
    
    def _init_(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        
    def _init_(self, word):
        self.word = word

    def _init_(self, word_guessed):
        self.word_guessed = word_guessed
    
    def _init_(self, num_letters):
        self.num_letters = num_letters
       
    def _init_(self, list_of_guesses):
        self.list_of_guesses = list_of_guesses
            
    def check_guess(self, guess):
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
    
    def ask_for_input(self):
        while True:
            guess = input("Please, guess a letter:")
            guess = guess.lower()
            if  len(guess) > 1 or guess.isalpha() == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print ("You already tried that letter!")
            else:
                if len(guess) <= 1 and guess.isalpha() == True:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    print (self.list_of_guesses)
        return
              
game = Hangman()
game.ask_for_input()