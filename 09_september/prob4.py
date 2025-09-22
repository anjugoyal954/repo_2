words = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
results = []

for word in words:
    i = 0
    j = len(word) - 1
    same = True

    while i < j:
        if word[i] != word[j]:
            same = False
            break
        i = i + 1
        j = j - 1

    results.append(same)

print(results)
