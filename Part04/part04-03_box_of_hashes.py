def line():
    print("#" * 10)


def box_of_hashes(height):
    while height > 0:
        line()
        height -= 1


box_of_hashes(3)
