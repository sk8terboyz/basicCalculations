import math
try:
    grade = int(raw_input("Enter the grade: "))
    gradeStr = str(grade)

    if grade >= 90:
        print("Mark: A -- " + "grade: " + gradeStr)
    elif 90 > grade >= 80:
        print("Mark: B -- " + "grade: " + gradeStr)
    elif 80 > grade >= 70:
        print("Mark: C -- " + "grade: " + gradeStr)
    elif 70 > grade >= 60:
        print("Mark: D -- " + "grade: " + gradeStr)
    elif 60 > grade >= 50:
        print("Mark: F -- " + "grade: " + gradeStr)

except ValueError:
    print("You did not enter a number")
