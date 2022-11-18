import random

class Hangman:
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    list_of_guesses = []
    word = random.choice(word_list)
    word_guessed = ['_']
    num_letters = int()
    num_lives = 5
    
    def _init_(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']
        self.num_letters = int()
        self.list_of_guesses = []
            
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            for i in range(0, len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed= str(self.word_guessed)[:i] + guess + str(self.word_guessed)[i + 1:]
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
            guess = guess.lower()
            if  len(guess) > 1 or guess.isalpha() == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print ("You already tried that letter!")
            else:
                if len(guess) <= 1 and guess.isalpha() == True:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
        return
    
def play_game(word_list):
    game = Hangman(Hangman.num_lives, Hangman.word_list)
        
    while True:
        if Hangman.num_lives == 0:
            print ("You lost!")
            break
        elif Hangman.num_letters > 0:
            game.ask_for_input()
            
        elif Hangman.num_lives != 0 and Hangman.num_letters > 0:
            print ("Congratulations.You won the game!")
        break
    return

play_game(word_list)