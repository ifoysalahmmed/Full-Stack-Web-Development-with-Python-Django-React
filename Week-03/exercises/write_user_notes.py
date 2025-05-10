name = input("Enter your name: ")
message = input("Write a short message: ")

with open("user_notes.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Message: {message}\n")
