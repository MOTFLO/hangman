# Hangman
#### The Hangman is a game project that, which is defined along a five milestones, where each milestone is covering a set of functionalities of the game, based on Object Oriented Programming (OOP), using Python 3 as a programming language and Visual Studio Code as source-code editor for the program.

## Milestone 1
#### First milestone of the project is covering the fundamentals of the Python 3 programming language and setting up the virtual enviroment for the execution of the project, see the following:
* Python 3
* Visual Studio Code
* GitHub and Git

## Milestone 2
#### The milestone_2.py is a Python file, build in Python programming language, were are created variables, methods and functions for the Hangman game, using the VS Code. 
#### In Miletone 2 have been implemented the following functionalities: 
* How to define a list of possible words
* How to chose a random word from the list
* How to ask the user for an input
* How to check that the input is a single character

### Defining a list of possible words
```
# Creating a list contanning the names of 5 favorite fruits
# Assigning the list to a variable called word_list
# Using the print() function to print the word list variable

word_list = ["apple", "banana", "orange", "pear", "strawberry"]
print (word_list)
```
### Chosing a random word from the list
```
# Importing the "import random" to import the module for random method
# Creating the "random.choice" method and pass the word_list variable into
# Assigning the randomly generated word to a variable called "word"
# Printing the variable "word" using the print() function

random.choice(word_list)
word = random.choice(word_list)
print (word)
```
### Asking the user for an input
```
# Implemeting the "input" function to ask the user to enter a single letter
# Assigning the "input" function to a variable called "guess"

guess = input("Please enter a single letter:")
```
### Checking that the input is a single character
```
# Creating an "if" statement that checks if the lenght of the input is equal to 1 and the input is an alphabet
# "If" statement is met, then printing a message that says "Good guess!"
# Implementing an "else" block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

if len(guess) <= 1 and guess.isalpha () == True:
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")
```
## Milestone 3
### The milstone 3 is providing further information on how to define a function in oreder to use for a specific functionality. In the case scenarios have been implemented two types of fuctions, which are called for different type of process.
* A function that will take the guessed letter as an argument and and ckeck if the letter is in the word
* A function that is asking for an input from the user

### Defining a function that is checking the guess from the user
```
# Defining a function called "check_guess" and passing the "guess" as a parameter for the function
# Converting the input from the user into lower case using the method "guess.lower()"
# Checking the conditionalities if the guess is in the word, while the lenght of guess is meeting the criteria and is alphabet
# If the guess is in the word while loop has been satisfied, print the statment that says is a "Good guess!" and proiding option tp another try. 
# Else, print the "Sorry" statment and providing option to try again.
# Using the convert method, to convert the guess in lower case

def check_guess(guess):
    guess = guess.lower()
    while len(guess) <= 1 and guess.isalpha() == True:
        random.choice(word_list)
        word = random.choice(word_list)
        if guess in word:
            print ("Good guess!" + guess + " is in the " + word + ".")
        else:
            print ("Sorry, " + guess + " is not in the word. Try again.")
        guess = input("Please guess a letter:")
        guess = guess.lower()
        Break
    else:
        return check_guess
```
### Defining a function that is asking for input from the user
```
# Defining the function called "ask_for_input"
# Asking for the input from the user using the guees variable
# If the criteria is met of the guess variable when is ckecked by "check_guess" function and is in the random word, print the statment from "check_guess" function
# Else, print the following statment "Invalid letter. Please, enter a single alphabetical character." and return the function.
# Calling the function "ask_for_input" 

def ask_for_input():
    guess = input("Please guess a letter:")
    if check_guess(guess) == True and guess in check_guess.word(guess):
        print (check_guess)
    else:
        print ("Invalid letter. Please, enter a single alphabetical character.")
        return ask_for_input

ask_for_input()
```
## Milestone 4
#### In milestone 4 has been implemented the Object Oriented Programming (OOP), creating a game class Hangman, covering the following taks:
* How to create and initialise a class
* Creating methods for running the checks
* Defining what happens if the letter is in the word in "check_guess" method
* Defining what happens if letter in NOT in the word in "check_guess" method

### How to create and initialize a class
```
# First is created a class Hangman
# Within the class is defined the "_init_" methot to initialise the attributes of the self class, having the parameters "word_list" and "num_lives"
# Initializing other attribute within the "_init_" method: "word", "word_guessed", "num_letters", "num_lives" and the "list_of_guesses"

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

game = Hangman()
game.__init__()
```
### Creating methods for running the checks
```
# Defining a method "check_guess" method and passing the "guess" to the method as parameter
# Converting the "guess" variable input to lower case using "guess.lower()" method
# Creating an "if" block to verify if guess is in the word
# If the conditionality is met, then using the print function to print the following message "Good guess! {guess} is in the word."

def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + guess + " is in the word.")


# Defining a method called "ask_for_input" which is asking the user for input
# Creating a while loop and if it is "True" do the following
# Ask the user to guess a letter using the variable called "guess"
# Creating an "if" statement that runs if the guess is NOT a single alphabetical character
# Using the "print" function to print a message saying "Invalid letter. Please, enter a single alphabetical character."
# Creating an "elif" statement that checks if the "guess" is already in the "list_of_guesses"
# Using the "print" function to print a message saying "You already tried that letter!", if "elif" statement has not been met
# If the guess is a single alphabetical character and it's not already in the list_of_guesses, then do the following
# Creating an "else" block and calling the "check_guess" method and passing "guess" as an argument to this method
# Then, adding the "guess" to the "list_of_guesses" using the "list_of_guesses.append()" method

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
```
### Defining what happens if the letter is in the word in "check_guess" method
```
# Replacing the underscore(s) in the "word_guessed" with the letter guesssed by the user input
# Creating a for-loop that will loop through each letter in the word
# Within the for-loop, is implemented an "if" statement that checks if the letter is equal to the "guess"
# In the if block, replacing the corresponding "_" in the "word_guessed" with the guess and indexing the "word_guessed" at the position of the letter and assigning it to the letter
# Outside the loop, variable "num_letters" is reduced by 1

            for char in self.word:
                if char == guess:
                    indices = (i for i, c in enumerate(self.word) if c == guess)
                    for i in indices:
                        self.word_guessed[i] = guess
            print (self.word_guessed)
            self.num_letters -= 1
```
### Defining what happens if letter in NOT in the word in "check_guess" method
```
# Within the "check_guess" method is created an "else" statement as a continuity of the method
# If the above conditions has not been met, then do the following
# Redure the number of lives "num_lives" by 1
# Using the "print" function, print a message saying "Sorry, {letter} is not in the word."
# Using the "print" function, print another message saying "You have {num_lives} lives left."
# Aappending the guess to the "list_of_guesses" using the "list_of_guesses.append()" method
# Returning "ckeck_guess" method

        else:
            self.num_lives -= 1
            print ("Sorry, " + guess + " is not in the word.")
            print ("You have " + str(self.num_lives) + " lives left.")
            self.list_of_guesses.append(guess)
            print (self.list_of_guesses)
        return
```
Note: For a complete code program, see the "milestone_4.py" file.

## Milestone 5
#### The logic of the Hangman game is to play the game as long the number of lives are not exceeded and the letter is in a word that have to be guessed. If the guess letter is in the random word from the list, wich is implemented in the game, the word will be reconstructed guess by guess, taking an input from the user.
#### Every time a letter is not a match, the number of lives for the player is decreasing by 1. When the number of lives is 0, the player has lost the game.
#### The creation of the Hangman game is based on Object Oriented Programming (OOP) a number of factors as:
* Defining a class
* Implementing variables for the class
* Initialiasing the variables within the class
* Implementing and defining methods within the class
* Calling the class methods to run the game
* Instantiation of the class