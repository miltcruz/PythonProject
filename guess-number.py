import random


secret_number: int = random.randint(1, 10)
print(secret_number)  # For testing purposes, you can comment this out in production

guess: int = 0

while guess != secret_number:
    guess_input: str = input("Guess the number between 1 and 10: ").strip()

    if not guess_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 10.")
        continue

    guess = int(guess_input)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")

