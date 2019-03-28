# Created input prompt to save integer as variable num
num = input("Please enter a positive integer: ")
# Converted string to integer
num = int(num)
# Created an empty variable to collect the sum of all integers
sum = 0
# Created a for loop too iterate through from one up to num
for i in range(1, num + 1):
    # Added the current sum with the number being iterated over and over
    sum = sum + i
# Print final result
print(sum)