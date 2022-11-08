import random

class Hangman():
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    num_lives = 5
    
    random.choice(word_list)
    word = random.choice(word_list)
    
    word_guessed = ['_', '_', '_', '_', '_']
    num_letters = int()
    list_of_guesses = []
    
    def check_guess(guess, word):
        gues = guess.lower()
        if guess in word:
            print ("Good guess! " + guess + " is in the word.")
        return
    
        
    
    def ask_for_input(list_of_guesses, check_guess, word):
        while True:
            guess = input("Please, enter a letter:")
            guess = guess.lower()
            if  len(guess) > 1 or guess.isalpha() == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print ("You already tried that letter!")
            else:
                if len(guess) <= 1 and guess.isalpha() == True:
                    check_guess(guess, word)
                    list_of_guesses.append(guess)
                    print (list_of_guesses)
        return
               
    ask_for_input(list_of_guesses, check_guess, word)
        
_init_ = Hangman()