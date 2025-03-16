import sys
from stats import get_num_words, get_character_count, sort_character_dict

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
        sys.exit(1)
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    character_count = get_character_count(book_text)
    sorted_characters = sort_character_dict(character_count)

    print("-" * 12 + " BOOKBOT " + "-"*12)
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")

    # print("--------- Character Count -------")
    for character, count in sorted_characters.items():
        if character.isalpha():
            print(f"{character}: {count}")


if __name__ == "__main__":
    main()