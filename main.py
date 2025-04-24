from stats import get_num_words, get_num_chars


def get_book_text(file_path: str) -> str:
    '''
    Reads the content of a book from a given file path.

    :param file_path: The path to the book file.
    :return str: The content of the book as a string.
    '''

    with open(file_path, 'r') as f:
        file_contents = f.read()

    return file_contents


def main() -> None:
    '''
    Main function to execute the script.
    '''
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_nums = get_num_chars(book_text)
    print(f"{num_words} words found in the document")
    print(char_nums)


if __name__ == "__main__":
    main()
