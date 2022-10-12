def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c


number = greatest_number(3, 2, 1)
print(number)
