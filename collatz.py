# Question 4
"""
Resources:
1. To decern if the input was a string or an integer I had to use try and except.
I discovered how to use it at the following link. I use this in every other 
example where this is needed: https://pynative.com/python-check-user-input-is-number-or-string/
2. Needed a way to print the list nums without brackets, commas or quotes to 
match the question. Throung this post: https://www.quora.com/How-can-I-drop-brackets-in-a-Python-list-in-order-to-go-from-1-2-3-to-1-2-3 
on quora I found a way to run a for loop within the print statement to turn
each element to a string and join them with a space (i.e. " ").
"""
"""
TO DO:
"""

# Create prompt to collect input integer as variable.
num = input("Please enter a positive integer: ")
# Convert num from string to integer.
# Create list to hold numbers.
numsList = []
# Try this code and if no errors run this code.
try:
    # Convert input (num) to an integer.
    num = int(num)
    # While the variable num is less then one run this code.
    while num > 1:
        # If num is even.
        if (num % 2 == 0):
            # Devide it by 2.
            num = num / 2
            # Add this number to the list.
            numsList.append(int(num))
        # Else if num is odd.
        elif (num % 2 != 0):
            # Multiple by 3 and add 1.
            num = (num * 3) + 1
            # Add this number to the list.
            numsList.append(int(num))
    # Go through list and print as string and seperate each element with a space (ie " ")
    print(" ".join(str(a) for a in numsList))
# If there is an error run this instead.
except ValueError:
    # The error means the input wasn't and integer so print statement.
    print("This is not an integer. Please try again.")