def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")


spruce(5)
