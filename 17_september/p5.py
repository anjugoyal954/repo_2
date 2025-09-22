master_list = ["101", "102", "103", "104", "105", "106"] 

attended = open("attendance.txt", "r").read().splitlines()

present = []
absent = []

for roll in master_list:
    if roll in attended:
        present.append(roll)
    else:
        absent.append(roll)

print("Present students:")
for roll in present:
    print(roll)

print("\nAbsent students:")
for roll in absent:
    print(roll)

with open("absent.txt", "w") as f:
    for roll in absent:
        f.write(roll + "\n")
