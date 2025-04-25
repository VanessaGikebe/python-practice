
# Get input from user
number = int(input("Enter a positive number: "))

# Initialize factorial to 1
factorial = 1

# Initialize counter
i = 1

# Check if the number is negative
if number < 0:
    print("Factorial doesn't exist for negative numbers")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    # Calculate factorial using a while loop
    while i <= number:
        factorial *= i
        i += 1
    
    # Display the result
    print(f"Factorial of {number} is {factorial}")