# Write your solution here
def list_sum(list1: list, list2: list):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result


a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))
