"""She sends you emails, but they’re all encrypted with the Caesar cipher!
The problem is, you don’t know which shift key she is using. 
The good news is, you know your
friend only speaks and writes English words
So if you can write a program to find the decoding
that produces the maximum number of words, you can probably find the right decoding"""

from Problem_Set4_Caesar_Cipher_Encoder import *


WORDLIST_FILENAME = "Problem_Set4_words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

# (end of helper code)
# -----------------------------------



def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext. 
    text: string
    returns: 0 <= int 27
    find_best_shift(wordlist, 'Pmttw,hdwztl!') => 8
    """
    most_matches = 0

    shift = 0

    for guess_shift in range(27):
        num_matches = 0
        print("^^^^ now trying: ", guess_shift)
        decoded_text = apply_coder(text, build_decoder(guess_shift))
        print("now decoded_text is: ", decoded_text)
        # split by white space
        decoded_text_list = decoded_text.split()
        print("now decoded_text_list is: ", decoded_text_list)
        for word in decoded_text_list:
            if is_word(wordlist, word):
                num_matches += 1
        if num_matches > most_matches:
            most_matches = num_matches
            shift = guess_shift
    
    return shift
    