# Question 4
"""
Resources:
To decern if the input was a string or an integer I had to use try and except.
I discovered how to use it at the following link. I use this in every other 
example where this is needed: https://pynative.com/python-check-user-input-is-number-or-string/
"""
"""
TO DO:

1. Get numbers to print on same line in cmd. (possibly appending a list and taking
out the seperators?).
"""

# Create prompt to collect input integer as variable
num = input("Please enter a positive integer: ")
# Convert num from string to integer
# Create array
sum = []
try:
    num = int(num)
    while num > 1:
        if (num % 2 == 0):
            num = num / 2
            print(int(num))
        elif (num % 2 != 0):
            num = (num * 3) + 1
            print(int(num))
except ValueError:
    print("This is not an integer. Please try again.")