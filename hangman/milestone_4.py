import random

class Hangman:
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    num_lives = 5
    
    random.choice(word_list)
    word = random.choice(word_list)
    
    word_guessed = ['_', '_', '_', '_', '_']
    num_letters = int('')
    list_of_guesses = []
    
_init_ = Hangman 