# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
start = 0

while height > start:
    print("#" * width)
    height -= 1
