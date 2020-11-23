# 4989 베르트랑 공준

# N까지 모든 소수를 구할때, 
# 2부터 N까지 배열에 모두 넣은후 소수가 아닌것들을 모두 체크해버린다
def prime_list(n):
    sieve = [True] * n
    
    # N의 최대 약수 = sqrt(N)이기 때문에 여기까지만 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
 
    return [i for i in range(2, n) if sieve[i] == True]
 
while 1:
    n = int(input())
    if n == 0:
        break
    primes = prime_list(2 * n + 1)
    print(len([i for i in primes if i > n]))