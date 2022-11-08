# Milestone 2
### The milestone_2.py is a Python file, build in Python programming language, were are created variables, methods and functions for the Hangman game, using the VS Code. 
### In Miletone 2 have been implemented the following functionalities: 
* How to define a list of possible words
* How to chose a random word from the list
* How to ask the user for an input
* How to check that the input is a single character

## Defining a list of possible words
```
# Creating a list contanning the names of 5 favorite fruits
# Assigning the list to a variable called word_list
# Using the print() function to print the word list variable

word_list = ["apple", "banana", "orange", "pear", "strawberry"]
print (word_list)
```
## Chosing a random word from the list
```
# Importing the "import random" to import the module for random method
# Creating the "random.choice" method and pass the word_list variable into
# Assigning the randomly generated word to a variable called "word"
# Printing the variable "word" using the print() function

random.choice(word_list)
word = random.choice(word_list)
print (word)
```
## Asking the user for an input
```
# Implemeting the "input" function to ask the user to enter a single letter
# Assigning the "input" function to a variable called "guess"

guess = input("Please enter a single letter:")
```
## Checking that the input is a single character
```
# Creating an "if" statement that checks if the lenght of the input is equal to 1 and the input is an alphabet
# "If" statement is met, then printing a message that says "Good guess!"
# Implementing an "else" block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

if len(guess) <= 1 and guess.isalpha () == True:
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")
```
# Milestone 3
### The milstone 3 is providing further information on how to define a function in oreder to use for a specific functionality. In the case scenarios have been implemented two types of fuctions, which are called for different type of process.
* A function that will take the guessed letter as an argument and and ckeck if the letter is in the word
* A function that is asking for an input from the user

## Defining a function that is checking the guess from the user
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
## Defining a function that is asking for input from the user
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