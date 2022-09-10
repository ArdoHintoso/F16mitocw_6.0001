# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

from random import choice
# import numpy as np

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # Non-Recursive Example
    seq_copy = list(sequence)
    seq_perm = []
    perm_lib = [sequence]

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    while len(perm_lib) < factorial(len(sequence)):    
        for i in range(len(sequence)):
            letter_choice = choice(seq_copy)
            seq_perm.append(letter_choice)
            seq_copy.remove(letter_choice)
        
        new_str = ''.join(seq_perm)
        seq_copy = list(sequence)
        seq_perm = []

        if new_str not in perm_lib: perm_lib.append(new_str)

    return print(perm_lib)

    # if len(sequence) == factorial(len(sequence)): return print(sequence)

    # if np.size(sequence) == 1:
    #     wip_str = []
    #     seq_array = list(sequence)
    # elif len(sequence[-1]) < len(sequence[-2]):
    #     wip_str = list(sequence[-1])
    #     for letters in wip_str: seq_array = list(sequence[-2]).remove(letters)     
    # else: 
    #     wip_str = []
    #     seq_array = list(sequence[-1])

    # letter_choice = choice(seq_array)

    # if len(seq_array) == 1: 
    #     wip_str.append(letter_choice)
    #     new_str = ''.join(wip_str)
    #     if new_str not in sequence: 
    #         sequence = list(sequence).append(new_str)
    #     else: del sequence[-1]
    #     get_permutations(sequence)
    # else:
    #     seq_array.append(letter_choice)
    #     wip_str.append(letter_choice)
    #     new_str = ''.join(wip_str)
    #     sequence = list(sequence).append(new_str)
    #     get_permutations(sequence) 


get_permutations("abc") 


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

