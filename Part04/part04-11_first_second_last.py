sentence = "once upon a time there was a programmer"


def first_word(sentence):
    first = sentence.split()[0]
    return first


def second_word(sentence):
    second = sentence.split()[1]
    return second


def last_word(sentence):
    last = sentence.split()[-1]
    return last


print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))
