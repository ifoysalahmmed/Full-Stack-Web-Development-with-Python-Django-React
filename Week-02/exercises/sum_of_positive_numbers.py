total = 0
user_input = int(input("Enter a positive number (0 to stop): "))

while user_input != 0:
    total += user_input
    user_input = int(input("Enter a positive number (0 to stop): "))

print("Total sum:", total)
