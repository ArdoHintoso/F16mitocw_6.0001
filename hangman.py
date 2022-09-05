# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from itertools import count
from operator import concat
from pickle import FALSE, TRUE
import random
import string
from xmlrpc.client import boolean
import sys 

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist) 

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    counter = 0
    all_guessed = False

    for letter in secret_word:
      if letter in letters_guessed: counter += 1

    if counter == len(secret_word): all_guessed = True

    return all_guessed 

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    good_guesses = []

    for letter in secret_word:
      if letter in letters_guessed: good_guesses.append(letter)
      else: good_guesses.append('_ ')

    return ''.join(good_guesses)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    good_guesses = []

    for letter in secret_word:
      if letter in letters_guessed: good_guesses.append(letter)    
      
    alpha_lib = list(string.ascii_lowercase)
    available_letters = list(alpha_lib)

    for letters in alpha_lib:
      if letters in good_guesses: available_letters.remove(letters)
    
    return ''.join(available_letters)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print(f"Welcome to Hangman! The secret word has {len(secret_word)} letters. You have 6 guesses.")

    count_remaining = 6
    letters_guessed = []
    alpha_lib = list(string.ascii_lowercase)

    while count_remaining != 0 and is_word_guessed(secret_word,letters_guessed) == False: 
      availble_letters = get_available_letters(letters_guessed) 

      print(f"\nRound Prep: You have {count_remaining} guesses left.\nHere are the letters that you haven't guessed yet:\n{availble_letters}") 
      
      guess = input("You have one guess per round. Go for it! Insert a lower case letter: ")

      if guess in alpha_lib: 
        letters_guessed.append(guess)
      else: 
        guess = input("Invalid. You may only input a lower chase letter in the English alphabet.\nWarning: the program will exit automatically if an invalid input is received again. Please retry: ")
        if guess in alpha_lib:
          letters_guessed.append(guess)
        else: sys.exit()

      
      if guess in secret_word: 
        print(f"Nice! The letter {guess} is indeed part of the secret word.")
      else: 
        print("Oops, better luck next time!")
        count_remaining -= 1

      print(get_guessed_word(secret_word,letters_guessed))

      if is_word_guessed(secret_word,letters_guessed) == True: print(f"Congrats! You have guessed the secret word: {secret_word}.")

      if count_remaining == 0: print(f"You have exhausted all your chances. See you next time! The word we were looking for: {secret_word}")

    return 


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
