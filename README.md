# BookBot

BookBot is a simple Python-based tool for analyzing text files of books. It provides word and character counts, helping you gain insights into the structure of the text. This is my first project from [Boot.dev](https://www.boot.dev).

## Features

- Counts the total number of words in a book.
- Counts the frequency of each character (case-insensitive).
- Filters and displays only alphabetic character statistics in a sorted format.

## Requirements

- Python 3.12 or higher
- A text file of a book (e.g., `.txt` files) from [Project Gutenberg](https://www.gutenberg.org/).

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-bot.git
cd book-bot
```

### 2. Install Python (if not already installed)

- **Windows**: Install Python from [python.org](https://www.python.org/)
- **MacOS** Use [Homebrew](https://brew.sh/)

```bash
brew install python
```

- **Ubuntu (WSL)**: Install Python via `apt`

```bash
sudo apt update
sudo apt install python3
```

### 3. Add a Book File

Download a `.txt` file of a book from [Project Gutenberg](https://www.gutenberg.org/) and place it in the `books/` folder.

For example:

```
books/
├── frankenstein.txt
```

### 4. Run the Script

Run the script from the terminal, providing the path to the book file as an argument:

```bash
python3 main.py books/frankenstein.txt
```

**EXAMPLE OUTPUT**

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 78452 total words
--------- Character Count -------
a: 45678
e: 42345
i: 32123
...
============= END ===============
```

**Notes**

- Ensure the book file is in **plain text** format (`.txt`).
- The script is case-insensitive and **EXCLUDES** spaces and special characters in the final report output.

### Compatibility

This project has been tested on the following platforms:

- **Windows** (via Command Prompt or PowerShell)
- **MacOS** (via Terminal)
- **Ubuntu (WSL)** (via Bash)

### Contributing

Feel free to fork this repository and submit a pull request for improvements or additional features.
