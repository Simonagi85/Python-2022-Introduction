def chessboard(size):
    for i in range(size):
        if i % 2 == 0:
            row = "10" * size
        else:
            row = "01" * size

        print(row[0:size])
        i += 1


chessboard(3)
