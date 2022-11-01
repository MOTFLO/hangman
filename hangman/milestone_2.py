import random


favorite_fruits = ["apple", "banana", "orange", "pear", "strawberry"]
word_list = favorite_fruits
print (word_list)

random.choice(word_list)
word = random.choice(word_list)
print (word)

guess = input("Please enter a single letter:")