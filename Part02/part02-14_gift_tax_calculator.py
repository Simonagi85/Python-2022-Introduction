# Write your solution here
gift = int(input("Value of gift: "))
taxes = 0

if gift < 5000:
    print("No tax!")
elif gift >= 5000 and gift < 25000:
    taxes = 100 + (gift - 5000) * 0.08
    print(f"Amount of tax: {taxes} euros")
elif gift >= 25000 and gift < 55000:
    taxes = 1700 + (gift - 25000) * 0.10
    print(f"Amount of tax: {taxes} euros")
elif gift >= 55000 and gift < 200000:
    taxes = 4700 + (gift - 55000) * 0.12
    print(f"Amount of tax: {taxes} euros")
elif gift >= 200000 and gift < 1000000:
    taxes = 22100 + (gift - 200000) * 0.15
    print(f"Amount of tax: {taxes} euros")
else:
    taxes = 142100 + (gift - 1000000) * 0.17
    print(f"Amount of tax: {taxes} euros")
