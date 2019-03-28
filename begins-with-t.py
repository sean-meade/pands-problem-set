# Question 2
"""
TO DO:
1. Test with input date rather then current date.
"""

# Import datetime module
import datetime
# If weekday is equal to Tuesday (1) or Thursday (3)
if datetime.datetime.today().weekday() == 1 | datetime.datetime.today().weekday() == 3:
    # Then print statement 
    print("Yes - today begins with a T.")
# Otherwise
else:
    # Print statement
    print("No - today does not begin with T.")