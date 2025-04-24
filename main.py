
def get_book_text(file_path: str) -> str:
    '''
    Reads the content of a book from a given file path.

    :param file_path: The path to the book file.
    :return str: The content of the book as a string.
    '''

    with open(file_path, 'r') as f:
        file_contents = f.read()

    return file_contents


def count_words(text: str) -> int:
    '''
    Counts the number of words in a given book.

    :param text: The content of the book as a `str`.
    :return int: The number of words in the book.
    '''
    words_list = text.split()
    return len(words_list)


def main() -> None:
    '''
    Main function to execute the script.
    '''
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
