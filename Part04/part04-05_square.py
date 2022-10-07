def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)


def square(size, character):
    i = 1
    while i <= size:
        line(size, character)
        i += 1


square(3, "x")
