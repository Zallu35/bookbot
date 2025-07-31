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
