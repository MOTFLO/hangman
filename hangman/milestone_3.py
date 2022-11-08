import random
from ast import Break

word_list = ["apple", "banana", "orange", "pear", "strawberry"]

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


def ask_for_input():
    guess = input("Please guess a letter:")
    if check_guess(guess) == True and guess in check_guess.word(guess):
        print (check_guess)
    else:
        print ("Invalid letter. Please, enter a single alphabetical character.")
        return ask_for_input

ask_for_input()   