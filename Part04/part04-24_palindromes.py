# Write your solution here
def palindromes(s: str):
    return s == s[::-1]


def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")


main()
