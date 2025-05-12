# example - 1
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# example - 2
while True:
    user_input = input("Enter a number greater than 10: ")
    if int(user_input) > 10:
        print("Thanks!")
        break
    print("Try again.")
