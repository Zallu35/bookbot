def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    wall = count_words(get_book_text("books/frankenstein.txt"))
    letter_count = count_characters(get_book_text("books/frankenstein.txt"))
    letter_list = sorting(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wall} total words")
    print("--------- Character Count -------")
    for k in letter_list:
        print(f"{k["char"]}: {k["num"]}")
    print("============= END ===============")
    
    #print(letter_count)

from stats import count_words, count_characters, sorting

main()