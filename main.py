import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    wall = count_words(get_book_text(sys.argv[1]))
    letter_count = count_characters(get_book_text(sys.argv[1]))
    letter_list = sorting(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wall} total words")
    print("--------- Character Count -------")
    for k in letter_list:
        print(f"{k["char"]}: {k["num"]}")
    print("============= END ===============")
    
    #print(letter_count)

from stats import count_words, count_characters, sorting

main()