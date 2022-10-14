# Write your solution here
number = int(input("Please type in a positive integer: "))

for x in range(number * (-1), number + 1):
    if x == 0:
        continue
    print(x)
