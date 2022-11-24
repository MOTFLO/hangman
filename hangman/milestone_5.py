import random

class Hangman:

    # word_list: List of words to be used in the game as parameters.
    # list_of_guesses: A number of guesse that is added to this list.
    # word: The word to be guessed picked randomly from the word_list.
    # word_guessed: A list of the letters of the word, with '_' for each letter not yet guessed.
    # num_letters: The number of UNIQUE letters in the word that have not been guessed yet.
    # num_lives: Number of lives the player has set as parameter.
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    list_of_guesses = []
    word = random.choice(word_list)
    word_guessed = ['_'] * len(word)
    num_letters = int(len(set(word)))
    num_lives = 5
    
    # The initialising method, to initialise the attributes of the class and passing in the word_list and num_lives as parameters.
    
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []
    
    # Defining a method called "check_guess" and passing the "guess" to the method as a parameter.
    # Converting the "guess" variable to lower case.
    # If statment checks if the "guess" is in the "word".
    # If the above condition is met, print the message "Good guess! " + guess + " is in the word."
    # For each letter in the "word" check if the letter is equal to the "guess" variable.
    # If the letter is equal to the "guess" variable then:
    # Guess is equal to each index letter that is enumerated in "word".
    # For the index in above variable "indices".
    # The index of each character ('_') in list "word_guessed" is replaced by "guess" variable.
    # Printing the word guessed.
    # Reducing the variable "num_letters" by -1 for each letter guessed.
    # Else, if the "guess" variable is not in "word", reduce the number of lives by -1.
    # Printing the message saying "Sorry, " + guess + " is not in the word."
    # Printing the number of lives left.
    # Appeding the "guess" variable to the "list_of_guesses".
    # Printing the list of guesses that have been tested.
    # Return the method to send the function's result back to the caller.
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")
            for char in self.word:
                if char == guess:
                    indices = (i for i, c in enumerate(self.word) if c == guess)
                    for i in indices:
                        self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print ("Sorry, " + guess + " is not in the word.")
            print ("You have " + str(self.num_lives) + " lives left.")
            self.list_of_guesses.append(guess)
            print (self.list_of_guesses)
        return

    # Defining a method "ask_for_input" that is asking user for input.
    # A "guess" variable asking user for input.
    # Statement if the lenght of input is NOT a single alphabetical character:
    # Print the message saying that is invalid input.
    # If the letter is already in the "list_of_guesses":
    # Print a message saying "You already tried that letter!".
    # Else, if none of the above statements has not been met, call the "check_guess" method with the parameter "guess".
    # Appending the "guess" to the list of "list_of_guessed".
    # Return the method to send the function's result back to the caller.  

    def ask_for_input(self):
        guess = input("Please, guess a letter:")
        if  len(guess) > 1 or guess.isalpha() == False:
            print ("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print ("You already tried that letter!")
        else: 
            self.check_guess(self,guess)
            self.list_of_guesses.append(guess)
        return    


    # Defining a function called "play_game" that takes "word_list" as a parameter, to play the game.
    # An instance of the Hangman class, assigning to a variable called "game" and passing "word_list" and "num_lives" as arguments to the game object.
    # While loop condition is set to True:
    # If the "num_lives" it is 0, that means the game has ended and the user lost.
    # Print a message saying "You lost!".
    # Terminate the loop.
    # If the "num_letters" is greater than 0, continue the game.
    # Calling the "ask_for_input" method.
    # Else, if none of the above statements then:
    # Print a message saying "Congratulations! You have won the game!".
    # Terminate the loop.
    # Return the method to send the function's result back to the caller.

def play_game(word_list):
    game = Hangman(Hangman.word_list, Hangman.num_lives)
    while True:
        if Hangman.num_lives == 0:
            print("You lost!")
            break
        elif Hangman.num_letters > 0:
            Hangman.ask_for_input(Hangman)
        else:
            print("Congratulations! You have won the game!")
            break
    return

# Calling the "play_game" function to play the Hangman game and passing the "word_list" as argument to the function.

play_game(Hangman.word_list)