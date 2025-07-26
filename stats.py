def count_words(book_string):
    words = book_string.split()
    count = len(words)
    return count

def count_chars(book_string):
    chars = {}
    for char in book_string:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars