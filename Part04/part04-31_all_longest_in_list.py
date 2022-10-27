# Write your solution here
# Write your solution here
def all_the_longest(my_list: list):
    new_list = []
    longest = 0

    for item in my_list:
        if len(item) > longest:
            longest = len(item)

    for item in my_list:
        if len(item) == longest:
            new_list.append(item)

    return new_list


my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = all_the_longest(my_list)
print(result)
