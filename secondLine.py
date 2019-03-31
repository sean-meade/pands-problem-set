# Question 9
"""
I used the following link to understand how to slecect the
text file when passed as an argument in the command line:
https://docs.python.org/3/library/sys.html?highlight=sys
I also used stack over flow to find out how to remove the
break between lines when printing here: https://stackoverflow.com/questions/13374682/python-remove-enter-space-between-lines
"""
"""
TO DO:
"""
# Import system module
import sys

# set a varible to the second arguemnt from command line
fileName = sys.argv[1]

# Open file as read only
with open(fileName, 'r') as f:
    # Set a varible to count the lines.
    count = 0
    # For all the lines in the file.
    for i in f:
        # Add one to count.
        count = count + 1
        # If the count is even.
        if count % 2 == 0:
            # Print that line with out the new line escape sequence.
            print(i.rstrip("\n"))
            