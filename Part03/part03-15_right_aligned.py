# Write your solution here
x = input("Please type in a string:")

if len(x) < 20:
    print(x.rjust(20, "*"))
