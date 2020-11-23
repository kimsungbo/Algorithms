# 15652 N과 M
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

n, m = map(int, input().split())

num_list = list(range(1, n+1))

import itertools

combi = list(itertools.combinations_with_replacement(num_list, m))

for comb in combi:
    for i in range(len(comb)):
        print(comb[i], end=" ")
    print()