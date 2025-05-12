secret = 7

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    print("Wrong guess. Try again.")
