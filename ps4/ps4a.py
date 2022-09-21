# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

# from itertools import permutations 

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

    # USE_RECURSION
    permutations = []

    if len(sequence) == 1:
        return list(sequence)
    else: 
        for i in range(len(sequence)):
            new_additions = []
            seq_copy = list(sequence) 
            fixed_char = sequence[i]
            seq_copy.remove(sequence[i])
            
            for items in get_permutations(seq_copy): 
                new_additions.append(fixed_char + items)
            
            for new_strings in new_additions:
                if new_strings not in permutations: 
                    permutations.append(new_strings)

    return permutations 
    
    # # Non-Recursive Example
    # seq_copy = list(sequence)
    # seq_perm = []
    # perm_lib = [sequence]

    # def factorial(n):
    #     if n == 1:
    #         return 1
    #     else:
    #         return n * factorial(n-1)

    # while len(perm_lib) < factorial(len(sequence)):    
    #     for i in range(len(sequence)):
    #         letter_choice = choice(seq_copy)
    #         seq_perm.append(letter_choice)
    #         seq_copy.remove(letter_choice)
        
    #     new_str = ''.join(seq_perm)
    #     seq_copy = list(sequence)
    #     seq_perm = []

    #     if new_str not in perm_lib: perm_lib.append(new_str)

    # return perm_lib

    # Attempt at Recursive
    # if len(sequence) == factorial(len(sequence[0])) and len(sequence) > 2 : return print(sequence)

    # hist_str = []

    # if np.size(sequence) == 1:
    #     hist_str = [sequence]
    #     wip_str = []
    #     seq_array = list(sequence)
    # elif len(sequence[-1]) < len(sequence[-2]):
    #     # print(sequence[0])
    #     # print(sequence[1])
    #     for i in range(np.size(sequence)): 
    #         hist_str.append(sequence[i])
    #     wip_str = list(sequence[-1])
    #     prev_str = list(sequence[-2])
    #     for letters in wip_str: prev_str.remove(letters)
    #     seq_array = prev_str 
    # else: 
    #     for i in range(np.size(sequence)):  
    #         hist_str.append(sequence[i])
    #     wip_str = []
    #     seq_array = list(sequence[-1]) 

    # letter_choice = choice(seq_array)

    # if len(seq_array) == len(sequence[0]) and np.size(sequence) > 1: 
    #     wip_str.append(letter_choice)
    #     new_str = ''.join(wip_str)
    #     del hist_str[-2]
    #     if new_str not in sequence: 
    #         hist_str.append(new_str)
    #     else: del hist_str[-1] 
    #     get_permutations(hist_str) 
    # else: 
    #     wip_str.append(letter_choice)
    #     new_str = ''.join(wip_str)
    #     # if len(seq_array) > 1: del hist_str[-2]
    #     hist_str.append(new_str)
    #     get_permutations(hist_str) 

#     permutations = []

#     if len(sequence) == 1:
#         return sequence
#     else: 
#         for i in range(len(sequence)):
#             seq_copy = list(sequence)
#             seq_copy.remove(sequence[i])
#             this_loops_permutations = []  # 'a' + p('bc') == ['abc', 'acb']
#             new_string_permutations = get_permutations(seq_copy)  # ['bc', 'cb']
#             for each_permutation in new_string_permutations:
#                 this_loops_permutations.append(sequence[i] + each_permutation)
#             permutations.extend(this_loops_permutations)  # permutations.extend(['abc', 'acb'])
#         return permutations
    

# sequence = 'abcc'
# # output = get_permutations(sequence)
# # print(f'our output: {output}')

# output = get_permutations(sequence)
# print(output,len(output))

# itertools_output = [''.join(p) for p in permutations(sequence)]
# print(f'itertools output: {itertools_output}')

# print(f'matches: {output == itertools_output}')

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

