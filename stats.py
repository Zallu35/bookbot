def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    all_lower = text.lower()
    letters = {}
    for l in all_lower:
        if l in letters: 
            letters[l] +=1
        else:
            letters[l] = 1
    return letters

def sort_on(items):
    return items["num"]

def sorting(book_letters):
    just_letters = []
    for k in book_letters:
        if k.isalpha():
            just_letters.append({"char": k, "num": book_letters[k]})
    just_letters.sort(reverse=True, key=sort_on)    
    return just_letters