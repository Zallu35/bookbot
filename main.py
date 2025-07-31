def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    wall = get_book_text("books/frankenstein.txt")
    print(wall)

main()