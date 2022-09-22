# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

        return 

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = [*self.valid_words]

        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.         
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        shift_dict = {}
        ascii_letters = list(string.ascii_lowercase) 
        ascii_letters.extend(list(string.ascii_uppercase))

        for i in range(len(ascii_letters)):
            if (i + shift) >= 52: 
                shift_dict[ascii_letters[i]] = ascii_letters[i+shift-52]
            else: 
                shift_dict[ascii_letters[i]] = ascii_letters[i+shift]

        return shift_dict

    def apply_shift(self, shift): 
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        old_string = (self.get_message_text())
        old_string.split()
        new_string = []

        for i in range(len(old_string)):
            for letter in old_string[i]: 
                if letter in shift_dict:
                    new_string.append(shift_dict[letter])
                else:
                    new_string.append(letter)

        return ''.join(new_string) 

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.change_shift(shift) #set_or_update
        # self.shift = shift 
        # self.encryption_dict = self.build_shift_dict(self.shift)
        # self.message_text_encrypted = self.apply_shift(self.shift)
 

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encrypted_dict_copy = dict(self.encryption_dict)
        
        return encrypted_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''

        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

        return 


class CiphertextMessage(Message):
    def __init__(self, text): 
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        decrypted = []
        max_valid_words = 0 
        # matched_words = []

        for i in range(26):
            decrypted.append(self.apply_shift(i))
            # print(f'\n{i}, {decrypted}\n')
            
        for i in range(len(decrypted)):
            sentence = decrypted[i]
            best_shift = 0 
            # print(f"\n decrypted sentence: {sentence}")
            word_list = sentence.split()
            # print(f"\n{word_list}\n")
            for j in range(len(word_list)):
                if word_list[j].lower() in self.valid_words:
                    best_shift += 1
                    # matched_words.append(word_list[j])
        
            if best_shift >= max_valid_words:  
                best_sentence = (i, sentence)  # (decrypted.index(sentence), sentence)
                max_valid_words = int(best_shift)

            # if (decrypted.lower() or decrypted.upper()) in self.valid_words: 
            #     best_sentence.append((i,decrypted.lower()))
        
        # print(best_shift, max_valid_words)
        # print(matched_words,len(matched_words))

        plain_txt = PlaintextMessage(best_sentence[1],-best_sentence[0])
        print(plain_txt.get_message_text_encrypted())
        print(plain_txt.get_message_text_encrypted() == self.message_text)

        return best_sentence


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    # # TEST 1: 
    # original_message = Message(input("Insert a string: "))
    # print(original_message.build_shift_dict(26))
    # print(original_message.apply_shift(13))

    # # TEST 2: 
    # plain_txt = PlaintextMessage(input("Insert plain txt: "),14)
    # print(plain_txt.get_message_text_encrypted())
    # plain_txt.change_shift(1)
    # print(plain_txt.get_message_text_encrypted())
    # ciphertext = CiphertextMessage(plain_txt.get_message_text_encrypted())
    # print('Actual Output:', ciphertext.decrypt_message())

    #TODO: best shift value and unencrypted story 
    ciphertext = CiphertextMessage(get_story_string())
    print('\nActual Output:', ciphertext.decrypt_message())
