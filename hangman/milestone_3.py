import random
from ast import Break

guess = input("Please guess a letter:")
word_list = ["apple", "banana", "orange", "pear", "strawberry"]


while len(guess) <= 1 and guess.isalpha () == True:
    random.choice(word_list)
    word = random.choice(word_list)
    if guess in word:
        print ("Good guess!" + guess + " is in the " + word + ".")
    else:
        print ("Sorry, " + guess + " is not in the word. Try again.")
    guess = input("Please guess a letter:")
    Break
else:
    print ("Invalid letter. Please, enter a single alphabetical character.")
 