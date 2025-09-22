def list(lst):

    if len(set(lst)) != 5:
        return False

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            return False

    return True

print(list([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))  
print(list([1, 2, 3, 5, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))  
print(list([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 4, 5]))       

