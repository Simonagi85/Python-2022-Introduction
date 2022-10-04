# Write your solution here
password = "4321"
attempts = 0

while True:
    pin = input("PIN: ")
    attempts += 1

    if pin != password:
        print("Wrong")

    elif pin == password and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break

    elif pin == password and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
