from stats import count_words
from stats import count_chars

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        file_contents = book.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    result = f"{count} words found in the document"
    char_count = count_chars(book)
    print(result)
    print(char_count)

main()