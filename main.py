import sys
from stats import count_words
from stats import count_chars
from stats import sort_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

args = sys.argv

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        file_contents = book.read()
    return file_contents

def main():
    book = get_book_text(args[1])
    count = count_words(book)
    count_out = f"Found {count} total words"
    char_count = count_chars(book)
    sorted = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(count_out)
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()