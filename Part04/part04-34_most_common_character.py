# Write your solution here
def most_common_character(my_string: str):
    common = my_string[0]
    for i in my_string:
        if my_string.count(i) > my_string.count(common):
            common = i
    return common


first_string = "exemplaryelementary"
print(most_common_character(first_string))
