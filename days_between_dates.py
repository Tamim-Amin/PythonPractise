# Write a Python program to calculate the number of days between two dates

from datetime import date 

f_date=date(2025,10,9)
l_date=date(2025,11,9)
difference=l_date-f_date

print(difference.days)