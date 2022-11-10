import random

class Hangman:
    def _init_(self, num_lives, list_words):
        self.num_lives = num_lives
        self.word = random.choice(list_words)
        
    def check_letter(self, guess):
        self.guess = guess
        
    def ask_for_input(self):
        self
    
game = Hangman()
game.ask_for_input()