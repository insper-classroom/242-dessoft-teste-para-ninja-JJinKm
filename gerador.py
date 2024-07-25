import random

def gera_numeros():
    rand_list = [0]*4
    sum = random.randint(5,20)
    n1 = random.randint(2,20)
    n3 = random.randint(2,20)
    
    if n1 >= sum:
        while n1 >= sum:
            n1 = random.randint(2,20)

    n2 = sum - n1

    if sum - n3 == n2 or n3 == n2:
        while sum - n3 == n2 or n3 == n2:
            n3 = random.randint(2,20)

    rand_list[3] = sum
    i1 = random.randint(0,2)
    i2 = random.randint(0,2)
    i3 = random.randint(0,2)

    if i1 == i2 or i1 == i3 or i2 == i3:
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1 = random.randint(0,2)
            i2 = random.randint(0,2)
            i3 = random.randint(0,2)

    rand_list[i1] = n1
    rand_list[i2] = n2
    rand_list[i3] = n3
    
    return rand_list