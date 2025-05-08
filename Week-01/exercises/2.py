num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operation = str(input("Choose operation (+, -, *, /): "))

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/" and num2 != 0:
    print("Result:", num1 / num2)
elif operation == "/" and num2 == 0:
    print("Cannot divide by zero")
else:
    print("invalid operation!")
