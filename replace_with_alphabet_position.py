import string


def alphabet_position(input_string: str) -> str:
    """Replace every letter in the input string with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.
    a being 1, b being 2, etc. As an example:

    >>> alphabet_position("The sunset sets at twelve o' clock.")
    '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'

    Args:
        string (str): The input string.

    Returns:
        str: The output string with alphabet positions.
    """
    return " ".join(
        str(string.ascii_lowercase.index(letter) + 1)
        for letter in input_string.lower()
        if letter in string.ascii_lowercase
    )
