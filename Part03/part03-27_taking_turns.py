# Write your solution here
num = list(range(1, int(input("Please type in a number:")) + 1))

while num:
    print(num.pop(0))
    num.reverse()
