# Write your solution here
def anagrams(a: str, b: str):
    a1 = sorted(a)
    b1 = sorted(b)

    if a1 == b1:
        return True
    else:
        return False


print(anagrams("tame", "meta"))
