# Question 5
"""
TO DO:
"""
# Create prompt to take in integer as a variable
num = input("Please enter a positive integer: ")
# Create an empty variable to hold statement
statement = ""

# Try this block of code if no error run
try:
    # Convert input (num)to integer
    num = int(num)
    # If the input integer is equal to the prime numbers below 10.
    if (num == 2) | (num == 3) | (num == 5) | (num == 7):
        # Use "This is a prime number" statement
        statement = "This is a prime number."
    # If the input integer is equal to the numbers that are not prime below 10.
    if (num == 1) | (num == 4) | (num == 6) | (num == 8) | (num == 9):
        # Print this is not a prime number.
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
                    # If these conditions return true the loop will break
                    break
            # Otherwise the number is a prime.
            statement = "This is a prime number."
    # Else if the input num is less or equal to zero
    elif num <= 0:
        # It'll print that it is not positive and to try again.
        statement = "This is not a positive integer. Please try again."
    # If the number is less then 9 and not 2, 3, 5, or 7.
# If an error occurs then the input value (num) was not an integer so run this code
except ValueError:
    # Print this is not an integer.
    statement = "This is not an integer."
    
# Print whichever statement is returned.
print(statement)