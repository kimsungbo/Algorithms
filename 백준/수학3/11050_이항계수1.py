# 11050 이항계수1
# N개의 물건 중 순서를 고려하지 않고 K개를 고르는 경우의 수, 이항 계수를 구하는 문제

from math import factorial

n, k = map(int, input().split())

print(factorial(n) // (factorial(k) * factorial(n-k)))