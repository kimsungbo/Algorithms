# 9020 골드바흐의 추측

from itertools import product

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
 
    return [i for i in range(2, n) if sieve[i] == True]
 
n = int(input())

for _ in range(n):

    x = int(input())
    
    mid = x // 2
    
    prime_numbers = prime_list(x)

    # 차이가 작은 쌍을 구하기 위해 제일 큰수부터 확인
    for i in range(mid, 1, -1):
        # 두 수 모두 소수인지 확인
        if (x-i in prime_numbers) and (i in prime_numbers):
            print( i, x-i)
            break
