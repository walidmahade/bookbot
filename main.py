import sys
from stats import get_num_words, get_character_count, sort_character_count_dict

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_book_text(sys.argv[1])
    num_words = get_num_words(book_content)
    char_count = get_character_count(book_content)
    # print(char_count)
    sorted_char_count = sort_character_count_dict(char_count)
    # print(sorted_char_count)

    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
    """)

    for item in sorted_char_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()