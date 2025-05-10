age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

if age >= 17 and gpa >= 3.5:
    print("✅ You are eligible for admission!")
else:
    if age < 17:
        print("❌ Not eligible: You must be at least 17 years old.")
    else:
        print("❌ Not eligible: You must have a GPA of at least 3.5.")
