from itertools import permutations

def is_prime(x):
    
    if x != 1 and x != 0:
        for i in range(2, x):
            if(x % i == 0):
                return False
    else:
        return False
    return True

def solution(numbers):
    numbers= list(numbers)
    
    combis = []
    for i in range(1, len(numbers) + 1):
        combis.extend(list(permutations(numbers, i)))

    combis2 = []
    for tup in combis:
        temp_list = list(tup)
        combis2.append(int(''.join(temp_list)))
    combis2 = list(set(combis2))

    count = 0
    for com in combis2:
        if is_prime(com):
            count +=1
    return count