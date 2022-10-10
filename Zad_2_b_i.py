lista_liczb = [1, 2, 3, 4, 5]

def multiply_by_2(list):
    list = [list * 2 for list in list]
    return list

print(multiply_by_2(lista_liczb))