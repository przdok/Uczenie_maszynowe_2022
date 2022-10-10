number_list = [1, 2, 3, 4, 5]

def multiply_by_2(list):
    list2 = []
    for x in list:
        list2.append(x * 2)
    return list2

print(multiply_by_2(number_list))