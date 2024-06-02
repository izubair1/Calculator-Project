# Print a welcome message
print("Welcome to Simple Calculator!")

# Start an infinite loop to allow repeated calculations
while True:
    # Display the menu options
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Prompt the user for their choice
    choice = input("Enter choice (1/2/3/4/5): ")

    # Perform the selected operation
    if choice in ('1', '2', '3', '4'):
        # Get input numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation and display the result
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero!")
    # Exit the program if the user chooses option 5
    elif choice == '5':
        print("Exiting...")
        break
    # Notify the user if the input is invalid
    else:
        print("Invalid input! Please enter a valid option.")

# End of the program
