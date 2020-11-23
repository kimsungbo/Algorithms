# 2581 소수

def is_prime(x):
    if x != 1:
        for i in range(2, x):
            if(x % i == 0):
                return False
    else:
        return False
    return True

m = int(input())
n = int(input())

prime_list = []
for i in range(m, n+1):
    if is_prime(i):
        prime_list.append(i)

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)