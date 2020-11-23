# 2798 블랙잭
# 세장의 카드를 고르는 모든 경우를 고려하는 문제

import sys
from itertools import combinations

n, m = map(int, input().split())

cards = list(map(int, sys.stdin.readline().split()))

comb = [sum(x) for x in list(combinations(cards, 3))]

final_comb = []
for i in range(0, len(comb)):
    if(comb[i] <= m):
        final_comb.append(comb[i])
        
print(min(final_comb, key=lambda x:abs(x-m)))