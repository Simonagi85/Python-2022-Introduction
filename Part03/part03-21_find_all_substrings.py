# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = 0

while index < len(word) - 2:
    if word[i] == char:
        print(word[index : index + 3])
    index += 1
