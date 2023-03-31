#Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.

#has to be year first then month
#ensure to turn the inputs to integers
import calendar

ourMonth = int(input("Type in the month number:"))
ourYear = int(input("Type in the year number:"))

print(calendar.month(ourYear,ourMonth))