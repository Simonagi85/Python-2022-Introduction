# Write your solution here
def shortest(my_list: list):
    shortest = my_list[0]
    for item in my_list:
        if len(item) <= len(shortest):
            shortest = item
    return shortest


my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = shortest(my_list)
print(result)
