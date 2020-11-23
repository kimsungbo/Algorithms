# 11051 이항계수2
# 더 넓은 범위의 이항 계수를 동적 계획법을 사용하여 구하는 문제

from math import factorial

n, k = map(int, input().split())

print((factorial(n) // (factorial(k) * factorial(n-k))) % 10007)