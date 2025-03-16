from collections import Counter

def get_num_words(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    return Counter(letter.lower() for letter in book_text)

def sort_character_dict(character_dict):
    sorted_dict = dict(sorted(character_dict.items(), key=lambda item:item[1], reverse=True))
    return sorted_dict

