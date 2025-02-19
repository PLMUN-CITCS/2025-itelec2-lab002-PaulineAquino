# Your Name
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    # Introduce the program
    print("Simple Calculator Program")

    # Get user input and convert to integers
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    # Perform arithmetic operations and display results
    print(f"The sum is {num1 + num2}")
    print(f"The difference is {num1 - num2}")
    print(f"The product is {num1 * num2}")
    
    # Ensure division by zero is handled
    if num2 != 0:
        print(f"The quotient is {(num1 / num2):.2f}")
    else:
        print("The quotient is undefined (division by zero is not allowed).")

# Run the program
if __name__ == "__main__":
    main()
