# Write your solution here
def everything_reversed(my_list: list):
    reversed_list = []

    for item in my_list:
        reversed_list.append(item[::-1])
    return reversed_list[::-1]


my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
