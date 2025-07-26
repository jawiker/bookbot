from stats import count_words
from stats import count_chars
from stats import sort_dict

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        file_contents = book.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    count_out = f"{count} words found in the document"
    char_count = count_chars(book)
    sorted = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(count_out)
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    #print(sorted)

main()