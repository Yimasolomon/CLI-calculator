def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
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
        return "Addition selected"
    elif choice == "2":
        return "Subtraction selected"
    elif choice == "3":
        return "Multiplication selected"
    elif choice == "4":
        return "Division selected"
    elif choice == "5":
        return "Exiting calculator"
    else:
        return "Invalid choice. Please select 1-5"
