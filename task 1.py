# students marks
student_marks = {
    "Alice": 85,
    "ram": 60,
    "jay": 77
}
#command for asking student name
name = input("Enter the student's name: ")

#display of marks if found or else command
if name in student_marks:
    print(name + "'s marks:", student_marks[name])
else:
    print("Student not found.")