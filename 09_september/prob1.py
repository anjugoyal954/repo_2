n = int(input("Enter number of piles (and chocolates in first pile): "))
if n % 2 == 0:
    step = 2
else:
    step = 2

for i in range(n):
    print(n + i * step)
