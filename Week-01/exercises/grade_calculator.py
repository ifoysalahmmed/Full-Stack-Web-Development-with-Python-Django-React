name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("invalid marks")
elif marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80 and marks <= 89:
    grade = "A"
elif marks >= 70 and marks <= 79:
    grade = "B"
elif marks >= 60 and marks <= 69:
    grade = "C"
elif marks >= 50 and marks <= 59:
    grade = "D"
elif marks >= 0 and marks < 50:
    grade = "F"

if marks > 0 and marks < 100:
    print(f"Hello {name}! You scored {marks} and your grade is: {grade}")
