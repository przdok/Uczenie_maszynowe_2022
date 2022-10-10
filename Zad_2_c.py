list = [x for x in range(1, 11)]

def print_even(list):
    for x in list:
        if x % 2 == 0:
            print(x)

print(print_even(list))