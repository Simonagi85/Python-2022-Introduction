# Write your solution here
number_items = int(input("How many items: "))
list = []
i = 1

while i <= number_items:
    item = int(input(f"Input {i}: "))
    list.append(item)
    i += 1
print(list)
