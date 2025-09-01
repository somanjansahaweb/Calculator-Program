import math

def calculator():
    print("Advanced Calculator - Enter 'q' to quit")
    print("Operations: +, -, *, /, sin, cos, tan, sqrt, log, ln, ^")
    print("Note: Trigonometric functions use radians. Use 'deg' for degrees.")
    
    while True:
        try:
            # Get operation first to determine if we need one or two numbers
            operation = input("\nEnter operation (+, -, *, /, sin, cos, tan, sqrt, log, ln, ^ or 'q' to quit): ")
            
            if operation.lower() == 'q':
                print("Thank you for using the calculator!")
                break
            
            # Trigonometric and single-number operations
            if operation.lower() in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln']:
                num_input = input("Enter the number (or 'q' to quit): ")
                if num_input.lower() == 'q':
                    print("Thank you for using the calculator!")
                    break
                
                # Check if user wants degrees for trig functions
                if operation.lower() in ['sin', 'cos', 'tan']:
                    unit = input("Enter 'deg' for degrees or press Enter for radians: ")
                    if unit.lower() == 'deg':
                        num = math.radians(float(num_input))
                    else:
                        num = float(num_input)
                else:
                    num = float(num_input)
                
                # Perform single-number operations
                if operation.lower() == 'sin':
                    result = math.sin(num)
                    angle_str = f"{math.degrees(num)}°" if unit.lower() == 'deg' else f"{num} rad"
                    print(f"sin({angle_str}) = {result}")
                elif operation.lower() == 'cos':
                    result = math.cos(num)
                    angle_str = f"{math.degrees(num)}°" if unit.lower() == 'deg' else f"{num} rad"
                    print(f"cos({angle_str}) = {result}")
                elif operation.lower() == 'tan':
                    result = math.tan(num)
                    angle_str = f"{math.degrees(num)}°" if unit.lower() == 'deg' else f"{num} rad"
                    print(f"tan({angle_str}) = {result}")
                elif operation.lower() == 'sqrt':
                    if num < 0:
                        print("Error: Cannot calculate square root of negative number!")
                    else:
                        result = math.sqrt(num)
                        print(f"√{num} = {result}")
                elif operation.lower() == 'log':
                    if num <= 0:
                        print("Error: Logarithm undefined for non-positive numbers!")
                    else:
                        result = math.log10(num)
                        print(f"log₁₀({num}) = {result}")
                elif operation.lower() == 'ln':
                    if num <= 0:
                        print("Error: Natural logarithm undefined for non-positive numbers!")
                    else:
                        result = math.log(num)
                        print(f"ln({num}) = {result}")
            
            # Two-number operations
            elif operation in ['+', '-', '*', '/', '^']:
                # Get first number
                num1_input = input("Enter the first number (or 'q' to quit): ")
                if num1_input.lower() == 'q':
                    print("Thank you for using the calculator!")
                    break
                num1 = float(num1_input)
                
                # Get second number
                num2_input = input("Enter the second number (or 'q' to quit): ")
                if num2_input.lower() == 'q':
                    print("Thank you for using the calculator!")
                    break
                num2 = float(num2_input)
                
                # Perform two-number operations
                if operation == '+':
                    result = num1 + num2
                    print(f"{num1} + {num2} = {result}")
                elif operation == '-':
                    result = num1 - num2
                    print(f"{num1} - {num2} = {result}")
                elif operation == '*':
                    result = num1 * num2
                    print(f"{num1} * {num2} = {result}")
                elif operation == '/':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed!")
                    else:
                        result = num1 / num2
                        print(f"{num1} / {num2} = {result}")
                elif operation == '^':
                    result = math.pow(num1, num2)
                    print(f"{num1}^{num2} = {result}")
            
            else:
                print("Invalid operation! Available operations:")
                print("Basic: +, -, *, /, ^")
                print("Trigonometry: sin, cos, tan")
                print("Other: sqrt, log, ln")
            
            print("-" * 40)  # Separator line for readability
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator
