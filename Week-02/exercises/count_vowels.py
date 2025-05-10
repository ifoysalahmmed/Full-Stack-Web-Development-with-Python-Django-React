word = input("Enter a word: ")
word = word.lower()
vowels = "aeiou"
counter = 0

for i in word:
    if i in vowels:
        counter += 1

print(f"Number of vowels: {counter}")
