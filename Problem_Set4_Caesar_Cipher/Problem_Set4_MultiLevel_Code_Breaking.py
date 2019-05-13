"""apply_shifts("Do Androids Dream of Electric Sheep?", [(0, 6), (3, 18), (12, 16)]) 
'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'

find_best_shift(wordlist, 'Pmttw,hdwztl!') => 8
"""

from Problem_Set4_Caesar_Cipher_Encoder import *
from Problem_Set4_Code_breaking import find_best_shift, \
                                        load_words, is_word
from Problem_Set4_MultiLevel_Encryption import apply_shifts

import time
import random


#==========start of helper function
def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    print("s is: ", s)
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("Problem_Set4_fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable

#=========end of helper function


WORDLIST_FILENAME = "Problem_Set4_words.txt"
wordlist = load_words()


def find_best_shift_from_start(wordlist, text):
    shift = 0
    index = 0
    most_matches = 0

    final_decoded = []

    for guess_shift in range(28):
        num_matches = 0
        temp_index = 0
        #print("^^^^ now trying: ", guess_shift)
        decoded_text = apply_coder(text, build_decoder(guess_shift))
        #print("now decoded_text is: ", decoded_text)
        decoded_text_list = decoded_text.split()
        #print("now decoded_text_list is: ", decoded_text_list)
        for word in decoded_text_list:
            if is_word(wordlist, word):
                num_matches += 1
                temp_index += len(word) + 1
                # print(num_matches, temp_index)
                final_decoded.append(word)
            else:
                break
        if num_matches > most_matches:
            most_matches = num_matches
            shift = guess_shift
            index = temp_index
    #print("$$$$ shift and index are: ", shift, index)
    return index, shift

def find_best_shifts_rec(wordlist, text, start):
    """
    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples. each tuple is (position in text, amount of
    shift)
    """
    # time.sleep(1)
    if text=="":
        return []
    else:
        #print("now text is: ", text)
        index, shift = find_best_shift_from_start(wordlist, text)
        if index == 0:
            return []
        origin_pos = start
        start += index
        text = apply_coder(text, build_decoder(shift))
        return [(origin_pos, shift)] + find_best_shifts_rec(wordlist, text[index:], start)

def find_best_shifts(shifts):
    """ return the proper shifts for apply_shifts to decrypt message"""
    proper_shifts = []
    for s in shifts:
        pos, shift = s
        proper_shifts.append((pos, 27-shift))
    return proper_shifts

"""
temp = find_best_shifts_rec(wordlist, "JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?", 0)
temp2 = find_best_shifts_rec(wordlist, 'Pmttw,hdwztl!', 0)
temp3 = find_best_shifts_rec(wordlist, 'Pmttw,hgzbwo!', 0)
# apply_shifts("Hello, world!", [(0,8)]) -> 'Pmttw,hdwztl!'
# apply_shifts("Hello world!", [(0,8)]) -> 'Pmttwhhdwztl!'
# apply_shifts("Hello, world!", [(0,8), (7,3)]) -> 'Pmttw,hgzbwo!'
print(temp)
print(temp2)
print(temp3)

 >>> s
 'eqorqukvqtbmultiform wyy ion'
 >>> shifts = find_best_shifts_rec(wordlist, s, 0)
In [76]: shifts
Out[76]: [(0, 2), (11, 25), (21, 22)]

In [77]: find_best_shifts(shifts)
Out[77]: [(0, 25), (11, 2), (21, 5)]

 >>> apply_shifts(s, shifts)
 'compositor multiform accents'
"""

def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.
    returns: string - fable in plain text
    """
    encrypted_fable = get_fable_string()
    shifts = find_best_shifts_rec(wordlist, encrypted_fable, 0)
    shifts = find_best_shifts(shifts)
    decrypted_fable = apply_shifts(encrypted_fable, shifts)
    return decrypted_fable
