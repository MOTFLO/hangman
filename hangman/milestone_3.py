from ast import Break

guess = input("Please guess a letter:")
while len(guess) <= 1 and guess.isalpha () == True:
    print ("Good guess!")
    guess = input("Please guess a letter:")
    Break
else:
    print ("Invalid letter. Please, enter a single alphabetical character.")
    