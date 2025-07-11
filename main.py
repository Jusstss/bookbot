from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    word_count = count_words(contents)
    char_count = count_chars(contents)
    char_count = sort(char_count)

    print(f"============ BOOKBOT ============\n\
Analyzing book found at books/frankenstein.txt...\n\
----------- Word Count ----------\n\
Found {word_count} total words\n\
--------- Character Count -------\n")
    for value in char_count:
        print(f"{value["char"]}: {value["num"]}")

main()