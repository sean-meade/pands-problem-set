# Qustion 3
"""
TO DO:
"""
# Loop through numbers from 1000 to 10000
for i in range(1000, 10001):
    # if divisble by 6 and not by 12
    if (i % 6 == 0) & (i % 12 != 0):
        # Print that number
        print(i)