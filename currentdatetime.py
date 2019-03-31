# Question 8
"""
For this question I had to look up the function to call current date, time day ect.
I found a list of them along with the relevent function (strftime()) and how to use it here: 
https://www.w3schools.com/python/python_datetime.asp
"""
"""
TO DO:
"""
# Import datetime module
import datetime

# Set the datetime values of now as a variable
today = datetime.datetime.now()
# Set varible to store the weekday name
wday = today.strftime('%A')
# Set varible to store the month name
month = today.strftime('%B')
# Set varible to store the day of the month number
dayNo = today.strftime('%d')
# Set varible to store the year
year = today.strftime('%Y')
# Set varible to store current time
time = today.strftime('%X')
# Set varible to store whether or not if its am or pm
ampm = today.strftime('%p').lower()

# Set varible to store the day of the month number as an integer.
prefixNo = int(dayNo)
# Set varible to store epmty string for prefix of day of month
prefix = ''

# if the month day is equal to 1, 21 or 31 set prefix to "st"
if prefixNo == 1 | prefixNo == 21 | prefixNo == 31:
    prefix = "st"
# if the month day is equal to 2 or 22 set prefix to "nd"
elif prefixNo == 2 | prefixNo == 22:
    prefix = "nd"
# if the month day is equal to 3 or 23 set prefix to "rd"
elif prefixNo == 3 | prefixNo == 23:
    prefix = "rd"
# if the month day is greater than 3 and less than 21 or greater than 23 and 
# less than 31 set prefix to "th"
elif (prefixNo > 3 & prefixNo < 21) | (prefixNo > 23 & prefixNo < 31):
    prefix = "th"

# Print weekday followed by a comma follwed by month, day number and prefix,
# the year, the first 4 digits of the time and the am/pm (all commas (outside brackets) are 
# spaces within the print statement)
print(wday+",",month,dayNo+prefix,year,time[0:5]+ampm)