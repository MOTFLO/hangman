import random

class Hangman:
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    list_of_guesses = []
    word = random.choice(word_list)
    word_guessed = ['_'] * len(word)
    num_letters = int(len(word))
    num_lives = 5
    
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = int(len(self.word))
        self.list_of_guesses = []
            
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            for char in self.word:
                if char == guess:
                    indices = (i for i, c in enumerate(self.word) if c == guess)
                    for i in indices:
                        self.word_guessed[i] = guess
            print (self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print ("Sorry, " + guess + " is not in the word.")
            print ("You have " + str(self.num_lives) + " lives left.")
            self.list_of_guesses.append(guess)
            print (self.list_of_guesses)
        return
    
    
    def ask_for_input(self):
        while True:
            guess = input("Please, guess a letter:")
            if  len(guess) > 1 or guess.isalpha() == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print ("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        return
    
def play_game(word_list):
    game = Hangman(Hangman.word_list, Hangman.num_lives)  
    while True:
        if game.num_lives == 0:
            print ("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print ("Congratulations.You won the game!")
            break
    return

play_game(Hangman.word_list)