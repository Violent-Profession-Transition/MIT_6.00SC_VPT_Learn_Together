import string

def build_coder(shift):
    """
    apply a Caesar cipher to a letter 
    returns a dict
    shift: int -27-27
        Example: >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    upper_letters = " " + string.ascii_uppercase
    lower_letters = " " + string.ascii_lowercase
    result = {}
    for i in upper_letters:
        index = upper_letters.index(i)
        #if shift < 0:

        if 0 <= index + shift < len(upper_letters):
            result[i] = upper_letters[index + shift]
        else:
            result[i] = upper_letters[abs(len(upper_letters) - abs(index + shift))]
    for i in lower_letters:
        index = lower_letters.index(i)
        if 0 <= index + shift < len(lower_letters):
            result[i] = lower_letters[index + shift]
        else:
            result[i] = lower_letters[abs(len(lower_letters) - abs(index + shift))]
    return result

def build_encoder(shift):
    """Returns a dict that can be used to encode a plain text.
    shift: 0 <= int < 27
    returns: dict
    """
    return build_coder(shift)

def build_decoder(shift):
    """Returns a dict that can be used to decode an encrypted text
    shift: 0 <= int < 27
    returns: dict
    """
    return build_coder(-shift)

def apply_coder(text, coder):
    """Applies the coder to the text. Returns the encoded text.
     text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    # NOTE: python str is immutable
    text_copy = list(text)
    result = []
    for letter in text_copy:
        result.append(coder.get(letter, letter))
    return ''.join(result)

def apply_shift(text, shift):
    """Given a text, returns a new text Caesar shifted by the given shift
 offset.
    The empty space counts as the 27th letter
    apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    res = apply_coder(text, build_encoder(shift))
    return res