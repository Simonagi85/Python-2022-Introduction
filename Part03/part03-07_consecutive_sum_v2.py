limit = int(input("Limit: "))
number = 1
sum = 1
sentence = "1"

while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    sentence += f" + {number}"
print(f"The consecutive sum: {sentence} = {sum}")
