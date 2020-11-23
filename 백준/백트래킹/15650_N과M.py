# 15650 N과 M
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

n, m = map(int, input().split())

num_list = list(range(1, n+1))

from itertools import combinations
combi = combinations(num_list, m)

for comb in combi:
    for i in range(0, m):
        print(comb[i], end=" ")
    print()