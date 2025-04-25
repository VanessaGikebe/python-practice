# Get input from user
number = int(input("Enter a number: "))

# Check if the number is even or odd
#If a number is even, dividing by 2 gives a remainder of 0
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")