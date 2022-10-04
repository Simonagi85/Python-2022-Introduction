# Write your solution here
year = int(input("Please type in a year: "))

# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("That year is a leap year.")

elif (year % 4 == 0) and (year % 100 != 0):
    print("That year is a leap year.")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("That year is not a leap year.")
