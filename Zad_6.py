def merge_list(op1: list, op2: list) -> list:
    for x in op2:
        if x not in op1:
            op1.append(x)
    op1 = [op1 ** 3 for op1 in op1]
    return op1

list2 = [x for x in range(1, 7)]
list1 = [x for x in range(5, 11)]
print(merge_list(list1, list2))