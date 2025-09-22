def clean_text(text):
    new_text = ""
    for ch in text:
        if ch in ['.', ',', '!', '?', ';', ':']:
            continue
        else:
            new_text += ch
    return new_text

def count_words(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def main():
    file = open("story.txt", "r") 
    content = file.read()
    file.close()

    cleaned = clean_text(content)
    word_count = count_words(cleaned)

    n = int(input("Enter minimum frequency: "))
    print(f"\nWord frequencies ≥ {n}:")

    for word in word_count:
        if word_count[word] >= n:
            print(word, "→", word_count[word])

main()
