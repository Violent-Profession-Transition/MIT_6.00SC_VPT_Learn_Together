from Problem_Set3_Scrabble import *
import time


word_list = load_words()
#
#
# Problem #6A: Computer chooses a word
#
#

def flatten_hand(hand):
    flat_list = []
    for letter in hand.keys():
        for n in range(hand.get(letter)):
            flat_list.append(letter)
    return flat_list

def permutations(hand):
    flat_list = flatten_h
    for i in flat_list:
        break


def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find the word that gives the maximum value score, and return it.
    This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # for each word in the wordlist,
    # brute force check if any word
    # can be formed by the hand
    best_score = 0
    chosen_word = ''
    for word in word_list:
        # instead of passing the whole wordList
        # we can simply pass the list [word]
        # because word in [word] will evaluate to true
        if is_valid_word(word, hand, [word]):
            score = get_word_score(word, HAND_SIZE)
            if score > best_score:
                best_score = score
                chosen_word = word
    print("chosen word is: ", chosen_word)
    return chosen_word



#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    hand_copy = hand.copy()
    total_score = 0
    initial_handlen = calculate_handlen(hand)
    while calculate_handlen(hand_copy) > 0:
        print("Current Hand: ", end=" ")
        display_hand(hand_copy)
        word = comp_choose_word(hand_copy, word_list)
        if word == '':
            break
        # calculate valid word score
        result = get_word_score(word, initial_handlen)
        # add the total_score
        total_score += result
        print('"{}" earned {} points. Total: {} points'.format(
            word, result, total_score
            ))
        hand_copy = update_hand(hand_copy, word)
    print("Goodbye! Total score: {} points.".format(total_score))

#
# Problem #6C: Playing a game
#
#
def combined_play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = {}
    while True:
        user_input = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_input == "n":
            hand = deal_hand(HAND_SIZE)
            play_mode = input("Enter u to have yourself play, c to have the computer play: ")
            if play_mode == "u":
                play_hand(hand, word_list)
            elif play_mode == "c":
                comp_play_hand(hand, word_list)
        elif user_input == "r":
            if hand != {}:
                play_mode = input("Enter u to have yourself play, c to have the computer play: ")
                if play_mode == "u":
                    play_hand(hand, word_list)
                elif play_mode == "c":
                    comp_play_hand(hand, word_list)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif user_input == "e":
            return
        else:
            print("Invalid command.")
    

#
# Build data structures used for entire session and play game
#

