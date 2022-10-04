# Write your solution here
temp = float(input("Please type in a temperature (F): "))
to_celsius = (temp - 32) * 5 / 9

print(f"{temp} degrees Fahrenheit equals {to_celsius} degrees Celsius")

if to_celsius < 0:
    print("Brr! It's cold in here!")
