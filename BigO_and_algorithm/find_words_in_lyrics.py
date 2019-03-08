import re


no_surprises_lyrics = """
    A heart that's full up like a landfill
    A job that slowly kills you
    Bruises that won't heal
    You look so tired, unhappy
    Bring down the government
    They don't, they don't speak for us
    I'll take a quiet life
    A handshake of carbon monoxide
    With no alarms and no surprises
    No alarms and no surprises
    No alarms and no surprises
    Silent, silent
    This is my final fit
    My final bellyache
    With no alarms and no surprises
    No alarms and no surprises
    No alarms and no surprises, please
    Such a pretty house
    And such a pretty garden
    No alarms and no surprises
    No alarms and no surprises
    No alarms and no surprises, please
"""

no_surprises_lyrics = re.sub(r",", "", no_surprises_lyrics)

lyrics = []
for line in no_surprises_lyrics.lower().strip().split("\n"):
    lyrics = lyrics + line.strip().split(" ")

my_dict_lyrics = {}
def word_frequency(my_dict_lyrics, lyrics_list):
    for word in lyrics_list:
        if word in my_dict_lyrics:
            my_dict_lyrics[word] += 1
        else:
            my_dict_lyrics[word] = 1
    return my_dict_lyrics

my_dict_lyrics = word_frequency(my_dict_lyrics, lyrics)
print(my_dict_lyrics)

def find_most_common_word(lyrics_dict):
    values_array = lyrics_dict.values()
    max_value = max(values_array)
    max_words = []
    for word in lyrics_dict:
        if lyrics_dict[word] == max_value:
            max_words.append(word)
    return max_words, max_value

print(find_most_common_word(my_dict_lyrics))

def find_words_with_freq_cutoff(lyrics_dict, threshold):
    """
    return a list of tuples, each tuple is (list, int)
    containing the list of words ordered by their frequency
    """
    # extract the most_common_word from dict
    # append it to the list
    # then delete it from the stock of dict
    freq_cutoff_list = []
    max_words, max_value = find_most_common_word(lyrics_dict)
    while max_value >= threshold:
        freq_cutoff_list.append((max_words, max_value))
        for i in max_words:
            del(lyrics_dict[i])
        max_words, max_value = find_most_common_word(lyrics_dict)
    return freq_cutoff_list

print(my_dict_lyrics)
print(find_words_with_freq_cutoff(my_dict_lyrics, 9))
# python mutates both the alias and the object...
print(my_dict_lyrics)
