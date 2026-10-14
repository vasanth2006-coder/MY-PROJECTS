print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-250): "))
if mark1 < 0 or mark1 > 250:
    print("Invalid! Enter marks between 0 and 250.")
else:
    mark2 = float(input("Enter marks for Subject 2 (0-250): "))
    if mark2 < 0 or mark2 > 250:
        print("Invalid! Enter marks between 0 and 250.")
    else:
        mark3 = float(input("Enter marks for Subject 3 (0-250): "))
        if mark3 < 0 or mark3 > 250:
            print("Invalid! Enter marks between 0 and 250.")
        else:
            mark4 = float(input("Enter marks for Subject 4 (0-250): "))
            if mark4 < 0 or mark4 > 250:
                print("Invalid! Enter marks between 0 and 250.")
            else:
                total = mark1 + mark2 + mark3 + mark4
                percentage = (total / 1000) * 100

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

                print("\n----- Student Result -----")
                print("Student Name:", name)
                print("Total Marks:", total, "/ 1000")
                print("Percentage:", round(percentage, 2), "%")
                print("Grade:", grade)