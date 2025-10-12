# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

number=float(input("Enter the number: "))
differnce=number-17
if number>17:
    print(f"The differnce is : {abs(differnce)*2}")