# Create prompt to collect input integer as variable
num = input("Please enter a positive integer: ")
# Convert num from string to integer
num = int(num)
print(num)
while num > 1:
    if (num % 2 == 0):
        num = num / 2
        print(int(num))
    elif (num % 2 != 0):
        num = (num * 3) + 1
        print(int(num))