# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
from os import scandir
import random
from re import I
import string
from tkinter.messagebox import YES
from typing import final

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------
def transform_string(word):
    upper_case = list(string.ascii_uppercase)
    lower_case = list(string.ascii_lowercase)

    original_word_array = list(word)
    word_array = []

    for letter in original_word_array:
        if letter in upper_case:
            word_array.append(lower_case[upper_case.index(letter)])
        else:
            word_array.append(letter)

    return ''.join(word_array)

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    # upper_case = list(string.ascii_uppercase)
    # lower_case = list(string.ascii_lowercase)

    # for i in range(len(upper_case)):
    #     SCRABBLE_LETTER_VALUES[upper_case[i]] = SCRABBLE_LETTER_VALUES[lower_case[i]]

    word_array = list(transform_string(word))
   
    part_1 = 0
    
    for letter in word_array:
        if letter in SCRABBLE_LETTER_VALUES:
            part_1 += SCRABBLE_LETTER_VALUES[letter]

    part2_val = 7 * len(word) - 3 * (n-len(word)) 

    if 1 >= part2_val:
        part_2 = 1
    else:
        part_2 = part2_val

    p1_score = part_1 * part_2

    return p1_score 

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys(): 
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0 
    returns: dictionary (string -> int)
    """
    
    hand={'*':1}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS) 
        hand[x] = hand.get(x, 0) + 1 
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    word_array = transform_string(word)


    print(word_array)

    hand_dup = dict(hand) 

    for letter in word_array:
        if letter in hand.keys() and hand[letter] > 0: 
            hand_dup[letter] -= 1

    return hand_dup

# hand = {'j':2, 'o':1, 'l':1, 'w':1, 'n':2}
# display_hand(hand)
# new_hand = update_hand(hand, 'JOLLY')
# display_hand(new_hand)
# display_hand(hand)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    hand_dup = dict(hand)
    cond_1 = False
    cond_2 = False

    # word_list_dup = word_list[:]
    # word_array = list(word)

    new_word = transform_string(word)
    
    if '*' in new_word: 
        for i in range(len(VOWELS)):
            is_this_a_word = new_word.replace('*',VOWELS[i])
            if is_this_a_word in word_list: 
                cond_1 = True
                break
    else:
        if new_word in word_list: cond_1 = True

    
    is_valid_word = False 
    counter = 0

    for letter in new_word:
        if (letter in hand.keys() and hand_dup[letter] >=1) or (letter == '*' and letter >=1): 
            counter += 1
            hand_dup[letter] -= 1

    if counter == len(new_word): cond_2 = True

    # print(cond_1)
    # print(cond_2)
    if cond_1 and cond_2: is_valid_word = True

    return is_valid_word

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    hand_size = int(sum(hand.values()))

    return hand_size


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    total_score = 0 
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print("\nHere is your hand: ")
        display_hand(hand)
        # Ask user for input
        word = input("\nPlease spell a word from the letter(s) in your hand or type ! twice to exit program: ")
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else: 
            # If the word is valid:
            if is_valid_word(word,hand,word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(word, calculate_handlen(hand))
                print(f"Word Score: {word_score}")
                total_score += word_score
                print(f"Updated Score: {total_score}")
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("0 points for invalid word; updating hand...") 
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand,word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print(f"Game is over! Your total score is: {total_score}")
    # Return the total score as result of function
    return total_score

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    hand_copy = dict(hand)
    hand_keys = list(hand.keys())
    scrabble_keys = list(SCRABBLE_LETTER_VALUES.keys())
    final_hand = {}
    
    for i in range(len(hand_keys)):
        if letter == hand_keys[i]:
            new_letter = random.choice(scrabble_keys)
            final_hand[new_letter] = hand_copy[letter]
        else: 
            final_hand[(hand_keys[i])] = hand_copy[hand_keys[i]]

    return final_hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    total_score = 0 
    round_score = 0
    replay_counter = 1
    sub_counter = 1

    num_of_hands = int(input("Enter the number of hands: "))

    size_of_hand = int(input("Enter a number for your desired hand size: "))

    HAND_SIZE = size_of_hand - 1

    hand = deal_hand(HAND_SIZE)
    hand_copy = dict(hand)

    while num_of_hands > 0:
        while calculate_handlen(hand) > 0:
            print("\nCurrent hand: ")
            display_hand(hand)
            
            if sub_counter != 0:
                sub_yes_no = input("Would you like to substitute a letter? ") 
                if sub_yes_no == 'yes':
                    sub_with_what = input("Which letter would you like to replace? ")
                    hand = substitute_hand(hand,sub_with_what)
                    sub_counter -= 1
                    display_hand(hand)

            word = input("\nPlease enter a word or '!!' to indicate you are done: ")
        
            if word == '!!':
                break
            else: 
                if is_valid_word(word,hand,word_list):
                    word_score = get_word_score(word, calculate_handlen(hand))
                    total_score += word_score
                    round_score += word_score
                    print(f"{word} earned {word_score} point. Total: {total_score}")
                else:
                    print("0 points for invalid word; updating hand...") 
                hand = update_hand(hand,word)

        num_of_hands -= 1

        if num_of_hands > 0 and replay_counter != 0: 
            replay_yes_no = input("Would you like to replay the hand?")
            if replay_yes_no == 'yes' and replay_counter != 0: 
                hand = hand_copy
                total_score -= round_score
                replay_counter -= 1
                round_score = 0
            else: 
                hand = deal_hand(HAND_SIZE)
        else: hand = deal_hand(HAND_SIZE)

        
    print(f"Game is over! Your total score is: {total_score}")
    return total_score
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    # play_hand(deal_hand(HAND_SIZE),word_list)

