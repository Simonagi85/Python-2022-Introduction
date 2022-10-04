# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character: ")

index = word.find(character)

if index != -1 and len(word) >= index + 3:
    sub_string = word[index : index + 3]
    print(sub_string)
