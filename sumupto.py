# Question 1
"""
TO DO:
"""
# Created input prompt to save integer as variable num
num = input("Please enter a positive integer: ")

# Try this code for errors
try:
    # Converted string to integer
    num = int(num)
    # If num is greater than zero run this
    if num > 0:
        # Created an empty variable to collect the sum of all integers
        sum = 0
        # Created a for loop too iterate through from one up to num
        for i in range(1, num + 1):
            # Added the current sum with the number being iterated over and over
            sum = sum + i
        # Print final result
        print(sum)
    # Otherwise if the number is less then or equal to zero run code.
    elif num <= 0:
        # Print statement.
        print("This is not a positive integer. Please try again.")
# If there is an error run this code.

except ValueError:
    # The error will be caused by the input of a string or boolean so print statement.
    print("This is not a number. Please try again.")