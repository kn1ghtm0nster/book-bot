import sys

from stats import get_num_words, get_num_chars, format_stats, display_stats


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
    # book_path = "books/frankenstein.txt"
    terminal_inputs = sys.argv

    if len(terminal_inputs) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = terminal_inputs[1]
    print(f"Analyzing book found at {book_path}")

    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_nums = get_num_chars(book_text)
    print("--------- Character Count -------")

    character_stats = format_stats(char_nums)
    display_stats(character_stats)


if __name__ == "__main__":
    print("============ BOOKBOT ============")
    main()
    print("============= END ===============")
