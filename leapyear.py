# Create a python program to check if the year is a leap year or not.
# Leap a year is divisible by 4 but not divisible by 100
# Except if it is also divisible by 400

year = int(input("Enter the year\n"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year,"is not a leap year")
