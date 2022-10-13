# Write your solution here
list = []

while True:
    print(f"The list is now {list}")
    action = input("a(d)d, (r)emove or e(x)it:")
    if action == "d":
        item = len(list) + 1  # Value of item is length of the list + 1
        list.append(item)
    elif action == "r":
        list.pop(len(list) - 1)
    elif action == "x":
        break
print("Bye!")
