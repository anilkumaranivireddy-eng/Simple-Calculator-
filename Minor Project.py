# Simple Calculator - Minor Project
# Using Python Arithmetic Operators

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."

# Main calculator function
def calculator():
    print("=" * 40)
    print("    PYTHON CALCULATOR - MINOR PROJECT")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")
    print("8. Exit")
    
    while True:
        choice = input("\nEnter choice (1-8): ")
        
        if choice == '8':
            print("\nThank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\nResult: {num1} / {num2} = {result}")
                elif choice == '5':
                    print(f"\nResult: {num1} % {num2} = {modulus(num1, num2)}")
                elif choice == '6':
                    print(f"\nResult: {num1} ** {num2} = {exponent(num1, num2)}")
                elif choice == '7':
                    result = floor_divide(num1, num2)
                    print(f"\nResult: {num1} // {num2} = {result}")
            except ValueError:
                print("\nInvalid input! Please enter numbers only.")
        else:
            print("\nInvalid choice! Please select 1-8.")

# Run the calculator
calculator()
