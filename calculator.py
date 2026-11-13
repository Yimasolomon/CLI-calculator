def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def display_menu():
    print("===== CLI CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_user_choice():
    return input("Choose an operation: ")


def perform_operation(choice):
    if choice == "1":
        numbers = get_numbers()

        if numbers is None:
            return "Returning to main menu"
        
        first, second = numbers
        return add(first, second)
    elif choice == "2":
        numbers = get_numbers()

        if numbers is None:
            return "Returning to main menu"
        
        first, second = numbers
        return subtract(first, second)
    elif choice == "3":
        numbers = get_numbers()

        if numbers is None:
            return "Returning to main menu"
        
        first, second = numbers
        return multiply(first, second)
    elif choice == "4":
        numbers = get_numbers()

        if numbers is None:
            return "Returning to main menu"
        
        first, second = numbers
        return divide(first, second)
    elif choice == "5":
        return "Exiting calculator"
    else:
        return "Invalid choice. Please select 1-5"

def get_numbers():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        return first_number, second_number

    except ValueError:
        print("Invalid input. Please enter a number")
        return None

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        message = perform_operation(choice)
        print(message)

        if choice == "5":
            break

if __name__ == "__main__":
    main()