text = " Welcome to Django World!  "

print(text.strip())  # Remove leading and trailing whitespace
print(text.lstrip())  # Remove leading whitespace
print(text.rstrip())  # Remove trailing whitespace
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.title())  # Convert to title case
print(text.capitalize())  # Capitalize the first character
print(text.replace("Django", "Python"))  # Replace a substring
print(text.split())  # Split the string into a list of words
print(text.split("o"))  # Split the string by a specific character
print(text.find("Django"))  # Find the index of a substring
print(text.index("Django"))  # Find the index of a substring (raises error if not found)
print(text.count("o"))  # Count occurrences of a substring
print(len(text))  # Get the length of the string
print(text.startswith(" Welcome"))  # Check if the string starts with a substring
print(text.endswith("World!  "))  # Check if the string ends with a substring
print(text.isalnum())  # Check if the string is alphanumeric
print(text.isalpha())  # Check if the string contains only alphabetic characters
print(text.isdigit())  # Check if the string contains only digits