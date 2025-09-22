myset = set()
n = int(input("how many numbers: "))
for i in range(n):
    myset.add(int(input("Enter number: ")))
print("Unique numbers:", sorted(myset))
print("Total count", len(myset))
print("total sum", sum(myset))
average = sum(myset)/len(myset)
print("Avg", average)
print("max", max(myset))
print("min", min(myset))

