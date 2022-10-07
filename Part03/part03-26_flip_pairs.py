num = int(input("Please type in a number: "))

for x in range(1, num + 1, 2):
    if x + 1 <= num:
        print(x + 1)
    print(x)
