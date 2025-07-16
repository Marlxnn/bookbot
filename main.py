import sys
from stats import number_of_words
from stats import word_counter
from stats import char_counter
from stats import get_sorted_char_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        frankie = f.read()
        return frankie

def main():
        if len(sys.argv) != 2:
              print("Usage: python3 main.py <path_to_book>")
              sys.exit(1)
              
        book_contents = get_book_text(sys.argv[1])
        character_count = char_counter(book_contents)
        sorted_chars = get_sorted_char_list(character_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words(book_contents)} total words")
        print("--------- Character Count -------")

        for char_dict in sorted_chars:
                char = char_dict["char"]
                count = char_dict["num"]  
                if char.isalpha():
                        print(f"{char}: {count}")
        print("============= END ===============")

        
main()

