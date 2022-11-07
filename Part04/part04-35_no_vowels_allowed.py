# Write your solution here
def no_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for i in my_string:
        if i not in vowels:
            new_string = new_string + i
    return new_string


my_string = "this is an example"
print(no_vowels(my_string))
