list = [x for x in range(3,13)]

def print_every_second(list):
    list2 = []
    for x in range(len(list)):
        if(x % 2 == 0):
            list2.append(list[x])
    print(list2)

print_every_second(list)