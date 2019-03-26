from Problem_Set4_Caesar_Cipher_Encoder import *

import copy
def apply_shifts(text, shifts):
    """Applies a sequence of shifts to an input text
     Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18),
    (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    res = copy.copy(text)
    for t in shifts:
        start, shift = t
        res = res[:start] + apply_shift(res[start:], shift)
    return res