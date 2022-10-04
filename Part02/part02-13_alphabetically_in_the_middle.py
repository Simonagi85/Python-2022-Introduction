# Write your solution here
a1 = input("1st letter: ")
a2 = input("2nd letter: ")
a3 = input("3rd letter: ")

if a2 > a1 and a2 < a3:
    print(f"The letter in the middle is {a2}")
elif a3 > a2 and a3 < a1:
    print(f"The letter in the middle is {a3}")
elif a1 > a2 and a1 < a3:
    print(f"The letter in the middle is {a1}")
elif a1 < a2 and a1 > a3:
    print(f"The letter in the middle is {a1}")
elif a2 < a1 and a2 > a3:
    print(f"The letter in the middle is {a2}")
elif a3 > a1 and a3 < a2:
    print(f"The letter in the middle is {a3}")
