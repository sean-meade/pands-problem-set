# Question 7
"""
TO DO:
"""
# Import math module.
import math
# Set varible to hold input number.
num = input("Please enter a positive number: ")

# Try this code for errors
try:
    # Convert num to a float number
    num = float(num)
    # Get the square root of it and round to one decimal place
    sqrt = round(float(math.sqrt(num)), 1)
    # Print the statement below.
    print("The square root of",num,"is approx.",sqrt)
# If there is errors print this statement.
except ValueError:
    print("This is not a number. Please try again.")