sentence = ""
last_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end":
        break
    elif last_word == word:
        break
    else:
        last_word = word
        sentence += word + " "

print(sentence)
