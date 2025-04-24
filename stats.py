
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
    lower_cased_text = text.lower()

    for char in lower_cased_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def format_stats(stats: dict[str, int]) -> list[dict]:
    """
    Formats a dictionary of character stats into a list
    of dictionaries with valid characters and their counts.

    **NOTE :** This function filters out non-alphabetic characters.

    :param stats: A dictionary with characters as keys and their counts as values.
    :return list: A list of dictionaries with character stats.
    :rtype: list[dict]
    """
    result = []

    for key, value in stats.items():
        if key.isalpha():
            result.append({
                'char': key,
                'count': value
            })

    return sorted(result, key=lambda x: x['count'], reverse=True)


def display_stats(stats: list[dict]) -> None:
    """
    Displays the character stats in a formatted manner.

    :param stats: A list of dictionaries containing character stats.
    :return None:
    """
    for stat in stats:
        print(f"{stat['char']}: {stat['count']}")
