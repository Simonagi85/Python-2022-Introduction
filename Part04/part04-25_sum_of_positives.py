# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum


if __name__ == "__main__":
    print("The result is", sum_of_positives([1, -1, 2, -2, 3, -3]))
