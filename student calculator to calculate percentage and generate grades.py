print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

total = mark1 + mark2 + mark3
percentage = total / 3

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)