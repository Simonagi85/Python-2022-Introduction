# Write your solution here
def no_shouting(list: list):
    new_list = []
    for i in list:
        if i.isupper():
            continue
        else:
            new_list.append(i)
    return new_list


my_list = [
    "ABC",
    "def",
    "UPPER",
    "ANOTHERUPPER",
    "lower",
    "another lower",
    "Capitalized",
]
pruned_list = no_shouting(my_list)
print(pruned_list)
