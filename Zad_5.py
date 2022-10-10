def is_equal(op1: list, op2: int) -> bool:
    return op2 in op1

list = [x for x in range(1, 11)]
print(is_equal(list, 5))