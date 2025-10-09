# Write a Python program that prints the calendar for a given month and year.

import calendar

month=int(input("Enter the number of month: "))
year=int(input("Enter the number of year: "))

print(calendar.month(year,month))