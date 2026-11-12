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
    choice = input("Choose an operation: ")


def perform_operation(choice):
    if choice == "1":
        first, second = get_numbers()
        return add(first, second)
    elif choice == "2":
        first, second = get_numbers()
        return subtract(first, second)
    elif choice == "3":
        first, second = get_numbers()
        return multiply(first, second)
    elif choice == "4":
        first, second = get_numbers()
        return divide(first, second)
    elif choice == "5":
        return "Exiting calculator"
    else:
        return "Invalid choice. Please select 1-5"

def get_numbers():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    return first_number, second_number

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-5): ")

        message = perform_operation(choice)
        print(message)

        if choice == "5":
            break

if __name__ == "__main__":
    main()