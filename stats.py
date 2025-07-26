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

def sort_on_num(items):
    return items["num"]

def sort_dict(dict_object):
    return_list = []
    for obj in dict_object:
        num = dict_object[obj]
        new_dict = {"char":obj,"num":num}
        return_list.append(new_dict)
    
    return_list.sort(reverse=True,key=sort_on_num)
    return return_list

