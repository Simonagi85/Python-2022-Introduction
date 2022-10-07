import math

while True:
    num = int(input("Please type in a number: "))

    if num > 0:
        f = math.factorial(num)
        print(f"The factorial of the number {num} is {f}")
    else:
        print("Thanks and bye!")
        break
