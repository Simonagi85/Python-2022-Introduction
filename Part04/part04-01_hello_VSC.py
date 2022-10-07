editor = "visual studio code"

while True:
    user_input = input("Editor: ").lower()

    if user_input == editor:
        print("an excellent choice!")
        break
    elif user_input == "notepad" or user_input == "word":
        print("awful")
    else:
        print("not good")
