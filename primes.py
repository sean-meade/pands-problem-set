# Question 5
"""
TO DO:
1. Fix if input is strings/boolean.
"""

# Create prompt to take in integer as a variable
num = input("Please enter a positive integer: ")
# Create an empty variable to hold statement
statement = ""
try:
    # Convert input (num)to integer
    num = int(num)
    # If the input integer is equal to the prime numbers below 9
    if (num == 2) | (num == 3) | (num == 5) | (num == 7):
        # Use "This is a prime number" statement
        statement = "This is a prime number."
    if (num == 1) | (num == 4) | (num == 6) | (num == 8) | (num == 9):
        statement = "This is not a prime number."
    # Otherwise if the number is greater then 9
    elif num > 9:
        # Using a range from 2 to 9 (i)
        for i in range(2,10):
            # If input integer (num) when devided by any number between 2 and 9 (i)
            if num % i == 0:
                # And the input integer (num) is not equal to one.
                if num != 1:
                    # Print "This is not a prime."
                    statement = "This is not a prime number."
                    break
            # Otherwise the number is a prime.
            statement = "This is a prime number."
    elif num <= 0:
        statement = "This is not a positive integer."
    # If the number is less then 9 and not 2, 3, 5, or 7.
except ValueError:
    statement = "This is not an integer."
print(statement)