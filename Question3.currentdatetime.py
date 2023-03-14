#Write a Python program to display the current date and time.
#solution from: https://www.programiz.com/python-programming/datetime/current-datetime
#datetime solution: w3schools.com

#my attempt
# import datetime 
# print(datetime)

#after reviewing how to do this
from datetime import date

dateToday = date.today()
print("The date for today is", dateToday)
print("\n")
#playing around with different formats for date:
print("There are different ways to format the current date in Python:")
print("--------------")


currentDate = date.today()
#Format 1- day/month/year
formatDate1 = currentDate.strftime("%d/%m/%Y")
print("Format 1:", formatDate1)

#Format 2 - month name and day, year
#ex. September 4, 2014
formatDate2 = currentDate.strftime("%B %m, %Y")
print("Format 2:", formatDate2)

#Format 3- Day of week, Month and day, year
#ex. Sunday, October 3, 2003
formatDate3 = currentDate.strftime("%A, %b %d, %Y")
print("Format 3:", formatDate3)

#Show the current date and time
import datetime

currentDateTime = datetime.datetime.now()
print("--------------")
print("The current date and time is ")
print(currentDateTime)



