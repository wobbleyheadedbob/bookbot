import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def main():
    #file_path = "books/frankenstein.txt"
    arg_length = len(sys.argv)

    try: 
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        num_words = get_word_count(book_text)
        words_dict = get_char_count(book_text)
        sorted_chars = sort_char_count(words_dict) 
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        #print(f"derp {sorted_chars}")
        for i in sorted_chars:
            char = i["char"]
            num = i["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")

    except Exception:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    

main()