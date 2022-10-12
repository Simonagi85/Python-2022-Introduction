def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)


def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1


triangle(3)
