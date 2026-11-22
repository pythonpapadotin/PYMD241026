students = ["Shyam", "Romeo", "Dele", "Dhamo", "Nitin"]

marks = {"Shyam": -89, "Romeo": -67, "Dhamo": -99, "Nitin": 0}

# Q1. Find all the students in the students list who did not gave the exam.
# Q2. Print the highest scorer name.
# Q3. Print If someone got below 60.

#  Till 8:38 PM IST
# students list who did not give the exam.

absent_students = []

for student in students:
    if student not in marks:
        absent_students.append(student)

print("Students who did not give the exam:", absent_students)

# highest scorer name.

highest_scorer = ""

highest_marks = float('-inf')

print('while float(-inf)', highest_marks)

for name, score in marks.items():
    if score > highest_marks:
        highest_marks = score
        highest_scorer = name

print("Highest scorer:", highest_scorer)

# someone got below 60.

below_60 = False

for name, score in marks.items():

    if score < 60:
        print(f"Q3 - {name} got below 60 ({score})")

        below_60 = True

if not below_60:
    print("No one got below 60")
