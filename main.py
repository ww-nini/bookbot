import sys

from stats import *


def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    filepath = sys.argv[1]
    content = get_book_text(filepath)

    print(f"Analyzing book found at {filepath}")

    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    result = transform_num_chars_dict(get_num_chars(content))
    for item in result:
        c = item["char"]
        n = item["num"]
        if c.isalpha():
            print(f"{c}: {n}")

if __name__ == '__main__':
    main()