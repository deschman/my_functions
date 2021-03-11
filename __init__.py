# -*- coding: utf-8 -*-
"""
Collection of miscellaneous user-defined functions.

@author: deschman
"""


# %% Imports
from typing import List


# %% Functions
def get_between(text: str, left_char: str = '(', right_char: str = ')') -> str:
    """
    Return substring between left_char and right_char.

    Rather than returning the next instance or the last instance of right_char,
    this function will count to ensure the returned substring has the same
    count of left_char and right_char inside it

    Parameters
    ----------
    text : str
        DESCRIPTION.
    left_char : str, optional
        DESCRIPTION. The default is '('.
    right_char : str, optional
        DESCRIPTION. The default is ')'.

    Returns
    -------
    between : str
        Substring between left_char and right_char where the count of left_char
        matches the count of right_char.

    """
    between: str = text[text.find(left_char):]
    substrings: List[str] = between.split(right_char)
    s: int = 0
    between = substrings[s] + right_char
    while between.count(left_char) != between.count(right_char):
        s+=1
        between = between + substrings[s] + right_char
    return between
