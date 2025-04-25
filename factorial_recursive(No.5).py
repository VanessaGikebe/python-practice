# Define a function that calculates the factorial of a number using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

# Ask the user to enter a number
num = int(input("Enter a non-negative integer: "))

# Check if the input is valid
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and print the result
    result = factorial(num)
    #Display result
    print(f"Factorial of {num} is {result}")
