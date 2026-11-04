students = []
count = int(input("Number of students: "))

for i in range(count):
    name = input("Name: ")
    marks = float(input("Average marks: "))
    attendance = float(input("Attendance percentage: "))
    income = float(input("Family income: "))

    if marks >= 80 and attendance >= 75 and income <= 500000:
        students.append((marks, attendance, income, name))

students.sort(key=lambda student: (-student[0], -student[1], student[2]))

quota = int(input("Scholarship quota: "))

for rank, (marks, attendance, income, name) in enumerate(students[:quota], start=1):
    print(rank, name, marks)
