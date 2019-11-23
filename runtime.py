def does_string_contain_letter(letter, string):
    """Determine whether a given letter is in a string."""

    if letter in string:
        return True
    return False


def duplicate_letters(string1, string2):
    """Determine whether there are duplicate letters in a string."""

    duplicates = []
    for letter in string1:
        if letter in string2:
            if letter not in duplicates:
                duplicates.append(letter)

    if duplicates:
        return True
    return False


def duplicate_letters_2(string1, string2):
    """Return a list of duplicate letters between two strings.
    If a letter appears more than once, the list should only contain the letter
    once.

    """

    duplicates = set()
    string2 = set(string2)
    for letter in string1:
        if letter in string2:
            duplicates.add(letter)

    return list(duplicates)
