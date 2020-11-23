# 1929 소수 구하기
# 에라토스테네스의 체 사용하여 소수 구하기

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

m, n = map(int, input().split())

for i in range(m, n+1):
    if is_prime(i):
        print(i)