#This defines a function called reverse_string that takes one input s (a string).
def reverse_string(s):
    # Initialize an empty string to store the reversed result
    reversed_str = ""

    # Loop through the string from the last character to the first
    for i in range(len(s) - 1, -1, -1):
        # Add the current character to the result
        reversed_str += s[i]

    # Return the reversed string
    return reversed_str

# Ask the user to enter a string
user_input = input("Enter a string to reverse: ")

# Call the function to reverse the string
reversed_result = reverse_string(user_input)

# Display the original and reversed strings
print("Original string:", user_input)
print("Reversed string:", reversed_result)
