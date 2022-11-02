import random

word_list = ["apple", "banana", "orange", "pear", "strawberry"]
print (word_list)

random.choice(word_list)
word = random.choice(word_list)
print (word)

guess = input("Please enter a single letter:")
if len(guess) <= 1 and guess.isalpha () == True:
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")
        