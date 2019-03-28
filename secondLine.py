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
import sys

fileName = sys.argv[1]

with open(fileName, 'r') as f:
    count = 0
    for i in f:
        count = count + 1
        if count % 2 == 0:
            print(i.rstrip("\n"))
            