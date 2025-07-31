def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    wall = count_words(get_book_text("books/frankenstein.txt"))
    letter_count = count_characters(get_book_text("books/frankenstein.txt"))
    print(f"{wall} words found in the document")
    print(letter_count)

from stats import count_words, count_characters

main()