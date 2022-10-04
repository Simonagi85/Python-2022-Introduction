# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily = hourly_wage * hours

if day != "Sunday":
    print(f"Daily wages: {daily} euros")
if day == "Sunday":
    print(f"Daily wages: {hourly_wage * 2 * hours} euros")
