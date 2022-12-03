import random

class Hangman:

    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    '''
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    list_of_guesses = []
    word = random.choice(word_list)
    word_guessed = ['_'] * len(word)
    num_letters = int(len(set(word)))
    num_lives = 5
    
    def __init__(self, word_list, num_lives):
        '''
        The constructor for the Hangman class.
        
        Parameters:
        ----------
        word_list: list
            List of words to be used in the game.
        num_lives: int
            Number of lives the player has.
        
        Attributes:
        ----------
        word: str
            The word to be guessed picked randomly from the word_list.
        word_guessed: list
            A list of the letters of the word, with '_' for each letter not yet guessed.
            For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
            If the player guesses 'a', the list would be ['a', '_', '_', '_', '_'].
        num_letters: int
            The number of UNIQUE letters in the word that have not been guessed yet.
        num_lives: int
            The number of lives the player has.
        list_of_guesses: list
            A list of the letters that have already been tried.
        
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []
    
    
    def check_guess(self, guess):
        '''
        The function checks if the letter is in the word_list.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        
        Parameters:
        ----------
        guess: str
            The letter to be checked.
        
        Returns:
        --------
            check_guess: method
        '''
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
            print ("List of guesses: " + str(self.list_of_guesses))
        return  

    def ask_for_input(self):
        '''
        The function asks for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        
        Variable:
        ---------
        guess: str
            Asks user to guess a letter.
            
        Returns:
        --------
        ask_for_input: method
        '''
        guess = input("Please, guess a letter:")
        if  len(guess) > 1 or guess.isalpha() == False:
            print ("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print ("You already tried that letter!")
        else: 
            self.check_guess(self,guess)
            self.list_of_guesses.append(guess)
        return

def play_game(word_list):
    '''
    The function to play the game and checks three things:
    1. Checks if the num_lives is 0. If it is, that means the game has ended.
    2. If the num_letters is greater than 0, then asks ask_for_input method. 
    3. If the num_lives is not 0 and the num_letters is not greater than 0, user won the game.
    
    Parameter:
    ----------
    word_list: list
        List of words to be used in the game.
    
    Variable:
    ---------
    game:str 
        Instance of Hangman class with the argument word_list and num_lives.
    
    Returns:
    --------
    play_game: method

    '''
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

play_game(Hangman.word_list)