from stats import *

def main():
    contents = get_book_text('books/frankenstein.txt')
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