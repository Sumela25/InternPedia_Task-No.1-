# Welcome message
def welcome_message():
    print("Hello and Welcome to the Simple Console-Based Calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")
    print("Type 'exit' to quit the application.\n")

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

# Function to get valid numbers from the user
def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'exit':
                return 'exit'
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main function to run the calculator
def calculator():
    welcome_message()
    
    result = None  # Stores the result of the previous calculation
    
    while True:
        # If there is no previous result, ask for the first number
        if result is None:
            num1 = get_number("Enter the first number (or type 'exit' to quit): ")
            if num1 == 'exit':
                break
            result = num1
        else:
            print(f"Current result: {result}")
            choice = input("Do you want to continue with the current result? (yes/no): ").lower()
            if choice == 'no':
                num1 = get_number("Enter the first number (or type 'exit' to quit): ")
                if num1 == 'exit':
                    break
                result = num1
        
        while True:
            # Get the operation
            operation = input("Enter operation (+, -, *, /) or type 'exit' to quit: ")
            if operation == 'exit':
                break
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please enter one of +, -, *, /.")
                continue
            
            # Get the second number
            num2 = get_number("Enter the next number (or type 'exit' to quit): ")
            if num2 == 'exit':
                break
            
            # Perform the operation
            if operation == '+':
                result = add(result, num2)
            elif operation == '-':
                result = subtract(result, num2)
            elif operation == '*':
                result = multiply(result, num2)
            elif operation == '/':
                result = divide(result, num2)
                if isinstance(result, str):  # If result is an error message
                    print(result)
                    break
            
            print(f"Result after operation: {result}")
        
        if operation == 'exit' or num2 == 'exit':
            break
    
    # Farewell message
    print("Thank you for using the calculator. See you again!")

# Run the calculator
if __name__ == "__main__":
    calculator()
