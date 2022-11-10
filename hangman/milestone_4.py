import random


class Hangman():
    
    word_list = ["apple", "banana", "orange", "pear", "strawberry"]
    num_lives = 5
    
    random.choice(word_list)
    word = random.choice(word_list)
    
    word_guessed = []
    num_letters = int()
    list_of_guesses = []
    
    def check_guess(list_of_guesses, guess, word, word_guessed, num_letters, num_lives):
        #gues = guess.lower()
        if guess in word:
            print ("Good guess! " + guess + " is in the word.")
            for i in range(0, len(word)):
                if word[i] == guess:
                    i = i + 1
                    word_guessed = str(i) + " : " + guess
                    print (word_guessed)
            num_letters -= 1
        else:
            num_lives = num_lives - 1
            print ("Sorry, " + guess + " is not in the word.")
            print ("You have " + str(num_lives) + " lives left.")
        list_of_guesses.append(guess)
        print (list_of_guesses)
        return
    
        
    
    def ask_for_input(list_of_guesses, check_guess, word, word_guessed, num_letters, num_lives):
        while True:
            guess = input("Please, enter a letter:")
            guess = guess.lower()
            if  len(guess) > 1 or guess.isalpha() == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print ("You already tried that letter!")
            else:
                if len(guess) <= 1 and guess.isalpha() == True:
                    check_guess(list_of_guesses, guess, word, word_guessed, num_letters, num_lives)
        return
        
    ask_for_input (list_of_guesses, check_guess, word, word_guessed, num_letters, num_lives)
        
_init_ = Hangman()