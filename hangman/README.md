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
