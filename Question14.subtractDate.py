# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

#my attempt
# date1 = (2014, 7, 2)
# date2 = (2014, 7, 11)

# print("The number of days between the first and second date is (not sure)")

#Correct attempt

from datetime import datetime

# the dates in the original string format
stringDate1 = "2014/7/2"
stringDate2 = "2014/7/11"

#convert the dates from string to date object

date1= datetime.strptime(stringDate1, "%Y/%m/%d")
date2= datetime.strptime(stringDate2, "%Y/%m/%d")

#find the difference in the dates (must be in date object form)

#the days after the difference variable incidates that we want to subtract the differene of the dates' days specifically
differenceDate = date2 - date1
print("The difference between the two dates is", differenceDate.days, "days.")
