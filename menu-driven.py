# Simple menu-driven program in Python

def show_menu():
    """Displays the menu options to the user."""
    print("Menu:")
    print("1. Yes / No Check")
    print("2. Compare Two Numbers")
    print("3. Work with Text")
    print("4. Exit")


# Boolean variable to control the menu loop
running: bool = True

while running:
    # Display the menu to the user
    show_menu()

    # Get the user's choice
    choice: str = input("Please enter your choice (1-4): ").strip()

    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    choice = int(choice)

    if choice == 1:
        answer = input("Do you like Python? (yes/no): ").strip().lower()
        is_yes = answer == "yes"  # Boolean value from comparison
        if is_yes:
            print("Great! Python is very popular.")
        elif answer == "no":
            print("That's okay! Everyone has different preferences.")
        else:
            print("Please answer with 'yes' or 'no'.")

    elif choice == 2:
        num1_input = input("Enter the first number: ").strip()
        num2_input = input("Enter the second number: ").strip()

        if not num1_input.isdigit() or not num2_input.isdigit():
            print("Both inputs must be valid whole numbers.")
        else:
            number1 = int(num1_input)
            number2 = int(num2_input)

            is_greater = number1 > number2  # Boolean comparison

            if is_greater:
                print(f"{number1} is greater than {number2}.")
            elif number1 < number2:
                print(f"{number1} is less than {number2}.")
            else:
                print("Both numbers are equal.")

    elif choice == 3:
        text = input("Enter a word or phrase: ").strip()

        if text == "":
            print("You did not enter any text.")
        else:
            print("Uppercase:", text.upper())
            print("Lowercase:", text.lower())
            print("Length:", len(text))

    elif choice == 4:
        # Exit the program
        running = False
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
