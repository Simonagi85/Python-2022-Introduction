def length_of_longest(my_list: list):
    longest = len(my_list[0])
    for item in my_list:
        if len(item) > longest:
            longest = len(item)
    return longest


my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result)
