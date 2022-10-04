# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

attempts = 0
positive = 0
negative = 0
sum = 0

while True:
    number = int(input("Number: "))

    if number != 0:
        attempts += 1
        sum += number
        mean = sum / attempts

        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1

    else:
        break

print(f"Numbers typed in {attempts}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
