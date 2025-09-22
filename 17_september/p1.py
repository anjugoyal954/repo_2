lines = open("marks.csv", "r").readlines()

topper = {}  

for line in lines[1:]:
    parts = line.strip().split(",")
    name = parts[1]
    subject = parts[2]
    marks = int(parts[3])

    if subject not in topper or marks > topper[subject][1]:
        topper[subject] = (name, marks)

for subject in topper:
    name, marks = topper[subject]
    print("Subject:", subject, "→", name, "(", marks, ")")
