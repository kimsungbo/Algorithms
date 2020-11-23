import math

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if(x % i == 0):
                return False
    return True

def solution(n):

    num_prime = 0

    for num in range(1, n+1):
        if is_prime(num):
            num_prime +=1

    return num_prime