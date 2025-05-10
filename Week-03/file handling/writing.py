# Import the os module to work with the file system
# import os

# Get the directory of the current script file
# current_dir = os.path.dirname(os.path.abspath(__file__))
# Create a path to notes.txt in the same directory as this script
# file_path = os.path.join(current_dir, "notes.txt")

# Open the file at the specified path for writing
# with open(file_path, "w") as file:
with open("notes.txt", "w") as file:
    file.write("Learning Django is fun!\n")
    file.write("This is my first file.\n")
