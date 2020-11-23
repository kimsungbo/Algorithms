# 9461 파도반 수열
# 피보나치 수와 비슷한 규칙을 찾아 동적 계획법으로 푸는 문제

memo = {1:1, 2:1, 3:1, 4:2}

def pd(x):
    if x in memo:
        return memo[x]
    memo[x] = pd(x-2) + pd(x-3)
    return memo[x]

t= int(input())

for i in range(t):
    n = int(input())
    print(pd(n))