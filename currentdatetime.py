# Question 8
"""
For this question I had to look up the function to call current date, time day ect.
I found a list of them along with the relevent function (strftime()) and how to use it here: 
https://www.w3schools.com/python/python_datetime.asp
"""
"""
TO DO:

"""
import datetime

today = datetime.datetime.now()

wday = today.strftime('%A')
month = today.strftime('%B')
dayNo = today.strftime('%d')
year = today.strftime('%Y')
time = today.strftime('%X')
ampm = today.strftime('%p').lower()

prefixNo = int(dayNo)
prefix = ''

if prefixNo == 1 | prefixNo == 21 | prefixNo == 31:
    prefix = "st"
elif prefixNo == 2 | prefixNo == 22:
    prefix = "nd"
elif prefixNo == 3 | prefixNo == 23:
    prefix = "rd"
elif (prefixNo > 3 & prefixNo < 21) | (prefixNo > 23 & prefixNo < 31):
    prefix = "th"



print(wday+",",month,dayNo+prefix,year,time[0:5]+ampm)