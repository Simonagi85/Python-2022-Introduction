def distinct_numbers(my_list: list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    new_list.sort()
    return new_list


my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))
