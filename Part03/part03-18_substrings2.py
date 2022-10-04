# Write your solution here
string = input("Please type in a string: ")
l = len(string)

for i in range(l):
    print(string[l - 1 :])
    l -= 1
