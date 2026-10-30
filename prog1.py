import string

def find_rarest_word():
    text = input("Введите строку: ")
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.lower().translate(translator)
    words = clean_text.split()
    
    if not words:
        print("В тексте нет слов.")
        return

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    min_freq = min(freq.values())
    
    rarest_words = [word for word, count in freq.items() if count == min_freq]
    
    rarest_words.sort()
    
    print(f"Слово, которое встречается реже всего: {rarest_words[0]}")

if __name__ == "__main__":
    find_rarest_word()