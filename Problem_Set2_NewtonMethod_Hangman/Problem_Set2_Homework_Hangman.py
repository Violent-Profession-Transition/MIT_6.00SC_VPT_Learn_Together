# Problem #4
# Hangman
#
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random

WORDLIST_FILENAME = "Problem_Set2_words.txt"

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
    wordlist = str.split(line)
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

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
# wordlist = load_words()
# for local version
wordlist = ["haskell", "scoop", "data", "python", "google"]
print("loaded the words in wordlist:")
print(wordlist)

# your code begins here!
def generate_dash(chosen_word):
    dashed_hint = "_"
    for i in range(len(chosen_word)-1):
        dashed_hint = dashed_hint + " _"
    return dashed_hint

def replace_dash(letter, index_array, dashed_hint):
    list_dash = list(dashed_hint)
    for index in index_array:
        list_dash[index*2] = letter
    return "".join(list_dash)

def check_index(guess, chosen_word):
    index_array = []
    index = 0
    while index < len(chosen_word):
        # find the first occurrance
        index = chosen_word.find(guess, index)
        if index  == -1:
            break
        index_array.append(index)
        index += 1
    return index_array


chosen_word = choose_word(wordlist)
length_word = len(chosen_word)
dashed_hint = generate_dash(chosen_word)
num_guess = 10
print("Welcome to VPT's hangman!")
print("I am thinking of a word that is {} letters long".format(length_word))
print(">>>>>>>>>>>>>")
while num_guess > 0:
    if "_" not in dashed_hint:
        print("good job, you read my mind")
        break
    print(dashed_hint)
    print("you have {} guesses left".format(num_guess))
    guess = input("please guess a letter: ")
    if guess in chosen_word:
        print("Yay! correct guess!")
        dashed_hint = replace_dash(
                        guess,
                        check_index(guess, chosen_word),
                        dashed_hint)
    else:
        print("sorry, wrong guess...")
    num_guess -= 1
print("<<<<<<<<<<<<<")
if num_guess == 0:
    print("you ran out of guesses...")
print("the word i am thinking of is: ", chosen_word)
