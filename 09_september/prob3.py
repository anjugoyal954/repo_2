numbers1 = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
threshold1 = 100

numbers2 = [0, 12, 4, 3, 49, 9, 1, 5, 3]
threshold2 = 10

def indexes(numbers, threshold):
    indexes = []
    for i in range(len(numbers)):
        if numbers[i] < threshold:
            indexes.append(i)
    return indexes

print(indexes(numbers1, threshold1))
print(indexes(numbers2, threshold2))
