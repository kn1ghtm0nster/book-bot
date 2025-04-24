
def get_num_words(text: str) -> int:
    '''
    Counts the number of words in a given book.

    :param text: The content of the book as a `str`.
    :return int: The number of words in the book.
    '''
    words_list = text.split()
    return len(words_list)


def get_num_chars(text: str) -> dict[str, int]:
    '''
    Takes text from a book and returns 
    a dictionary with the number of times each character appears.

    spaces and special characters are included in the count.

    :param text: The content of the book as a `str`.
    :return dict: A dictionary with characters as keys and their counts as values.
    '''
    char_count = {}
    updated_text = text.lower()

    for char in updated_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
