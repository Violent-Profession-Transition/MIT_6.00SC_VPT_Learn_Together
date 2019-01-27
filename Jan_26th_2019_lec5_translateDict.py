English_to_Frensh_Dict = {
    "bread": "du pain",
    "wine": "du vin",
    "eats": "mange",
    "drinks": "bois",
    "likes": "aime",
    1: "un",
    "6.00": "6.00"
}

def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate_sentence(sentence):
    translation = ""
    sentence_words = sentence.split(' ')
    for word in sentence_words:
        result = translate_word(word, English_to_Frensh_Dict)
        translation = translation + result + ' '
    # remove the last white space at the end
    return translation.strip()

print(translate_word("drinks", English_to_Frensh_Dict))
print(translate_sentence("John drinks wine"))
print(translate_sentence("I likes to eat bread at 6.00 o clock"))

"""
bois
John bois du vin
I aime to eat du pain at 6.00 o clock
"""
