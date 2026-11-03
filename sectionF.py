# Given student records
records = [
    ('Asha', 'Python', 78),
    ('Asha', 'SQL', 82),
    ('Asha', 'Excel', 71),
    ('Ravi', 'Python', 55),
    ('Ravi', 'SQL', 61),
    ('Ravi', 'Excel', 49),
    ('Meena', 'Python', 92),
    ('Meena', 'SQL', 88),
    ('Meena', 'Excel', 95),
    ('Karan', 'Python', 64),
    ('Karan', 'SQL', 70),
    ('Karan', 'Excel', 58),
]

# 1. Build a set of courses
courses = set()

for who, course, marks in records:
    courses.add(course)

print(sorted(courses))

# 2. Build dictionary of student scores
scores = {}

for who, course, marks in records:
    if who not in scores:
        scores[who] = []
    scores[who].append(marks)

# 3. Calculate average and grade
averages = {}

for who, marks in scores.items():
    avg = sum(marks) / len(marks)

    if avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"

    averages[who] = avg

    print(f"{who:<8} avg={avg:.1f} grade={grade}")

# 4. Top student and overall average
top = max(averages, key=averages.get)
overall = sum(averages.values()) / len(averages)

print(f"Top: {top} | Overall average: {overall:.2f}")

# 5. Students above overall average
above = [who for who, avg in averages.items() if avg > overall]

print("Above overall:", above)

# 6. Smallest and largest marks
all_marks = [marks for who, course, marks in records]

extremes = (min(all_marks), max(all_marks))

print(extremes, type(extremes).__name__)

# 7. Why we used these data types
# Set stores unique courses, dictionary stores student scores,
# list stores multiple marks, and tuple stores fixed extremes.