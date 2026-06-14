students = {}
file = open("Python/data/school.txt", "r", encoding="utf-8")
data = file.read().split("\n")
try:
    for i in data:
        if i != "":
            name, grades = i.split(";")
            new_grades = []
            for grade in grades.split(","):
                new_grades.append(int(grade))    
            students[name] = new_grades
        else:
            pass
except:
    print("No students loaded")
file.close()
if len(students) == 0:
    print("No student loaded")

while True:
    choice = int(input("Enter 1 for add a student, 2 for add a grade for a student, 3 for show grades of a student" \
                    " 4 for a arithmetic mean of a student, 5 for delete a grade, 6 for end: "))
    if choice == 1:
        name = input("Enter the name of student you would like to add: ")
        if name in students:
            print("Student already exists")
        else:
            students[name] = []
    elif choice == 2:
        try:
            name = input("Enter the name of student you would like to add a grade: ")
            grade = int(input(f"Enter a grade you would like to assign to {name}: "))
            students[name].append(grade)
        except KeyError:
            print("The name you entered does not exist")
    elif choice == 3:
        try:
            name = input("Enter the name of the stdent you would like to see grades: ")
            for i in students[name]:
                print(i)
        except KeyError:
            print("The name you entered does not exist")
    elif choice == 4:
        try:
            name = input("Enter name of the student you would like to see arithmetic mean: ")
            cycles = 0
            num = 0
            for i in students[name]:
                num += i
                cycles += 1
            print(f"arithmetic mean of {name} is {num / cycles}")
        except (KeyError, ZeroDivisionError):
            print("The name you entered does not exist or the student does not have any grades")
    elif choice == 5:
        try:
            name = input("Enter the name of the student you would like to delete a grade: ")
            grade = int(input("Enter the grade you would like to delete: "))
            index = list(students[name]).index(grade)
            students[name].pop(index)
        except (KeyError, ValueError):
            print("The name or grade you entered does not exist")
    elif choice == 6:
        break
    else:
        print("You did not enter valid number")

file = open("Python/data/school.txt", "w", encoding="utf-8")
for name in students:
    grades = students[name]
    grades_text = ""
    for grade in grades:
        grades_text += str(grade) + ","
    grades_text = grades_text[:-1]
    file.write(f"{name};{grades_text}\n")
file.close()