
def get_num_words(text: str) -> int:
    '''
    Counts the number of words in a given book.

    :param text: The content of the book as a `str`.
    :return int: The number of words in the book.
    '''
    words_list = text.split()
    return len(words_list)
