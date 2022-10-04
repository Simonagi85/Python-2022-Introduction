# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week?"))

groceries_day = groceries / 7
lunch_week = price * times
weekly = groceries + (times * price)
daily = groceries_day + (times * price / 7)

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
