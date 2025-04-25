# Ask the user to enter a number
num = int(input("Enter a number: "))

# Initialize a variable to store the sum
sum_of_digits = 0

# Make a copy of the original number for display later(to the user)
original_num = num

# Loop until all digits are processed
while num > 0:
    digit = num % 10            # Get the last digit
    sum_of_digits += digit      # Add the digit to the sum
    num = num // 10             # Remove the last digit from the number

# Display the result
print(f"Sum of digits of {original_num} is {sum_of_digits}")
